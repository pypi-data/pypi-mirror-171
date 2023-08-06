import argparse
import logging
import pathlib
import re
import sys
from rich.markup import escape
from rich.markdown import Markdown
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.theme import Theme
from lkmlstyle.check import Config, check, logs_handler, parse_config
from lkmlstyle.rules import ALL_RULES
from lkmlstyle.exceptions import (
    InvalidRuleCode,
    LkmlstyleException,
    InvalidConfig,
    InvalidRule,
)

console = Console(theme=Theme({"code": "white on #2D3138"}))


def print_rules_table() -> None:
    table = Table(title="lkmlstyle Rules", show_lines=True)
    table.add_column("Code", justify="center")
    table.add_column("Rationale")

    for rule in sorted(ALL_RULES, key=lambda x: x.code):
        table.add_row(rule.code, Markdown(f"**{rule.title}**\n\n{rule.rationale}"))

    console.print(table)


def format_path(path: pathlib.Path) -> str:
    if str(path.parent) == ".":
        return f"[bold]{path.name}[/bold]"
    else:
        return f"[dim]{path.parent}/[/][bold]{path.name}[/bold]"


def format_error(message: str, title: str = "Error") -> Panel:
    return Panel(
        message,
        title=f"[bold red]{title}[/bold red]",
        width=80,
        padding=(1, 2),
    )


def check_style(args) -> None:
    try:
        config = parse_config() or Config()
        # CLI args override any ignores and selects in the config file
        config.override(select=tuple(args.select), ignore=tuple(args.ignore))
        ruleset = config.refine(ruleset=ALL_RULES)
    except InvalidConfig as error:
        console.print(
            format_error(
                "[bold red]Your config file isn't formatted "
                "correctly and couldn't be parsed.[/]"
                f"\n\n{error}."
                "\n\nlkmlstyle read the invalid config file from "
                f"{format_path(pathlib.Path.cwd() / 'lkmlstyle.yml')}"
            )
        )
        sys.exit(error.code)
    except InvalidRule as error:
        console.print(
            format_error(
                "[bold red]Couldn't create a rule with the specification provided.[/]"
                "\n\nUsually this "
                "is because you've missed a required argument or provided an incorrect "
                f"one. Have you used the correct rule type? "
                "The error message was:\n\n[code]{error}[/]"
                "\n\nlkmlstyle read the invalid config file from "
                f"{format_path(pathlib.Path.cwd() / 'lkmlstyle.yml')}"
            )
        )
        sys.exit(error.code)
    except InvalidRuleCode as error:
        console.print(
            format_error(
                "[bold red]Invalid rule code.[/]"
                f"\n\n{error}. Run [code]lkmlstyle rules[/] to see all valid rule codes."
                "\n\nlkmlstyle read your config file from "
                f"{format_path(pathlib.Path.cwd() / 'lkmlstyle.yml')}"
            )
        )
        sys.exit(error.code)

    failed = False

    paths = []
    for path in args.path:
        if path.is_dir():
            paths.extend(path.glob("**/*.lkml"))
        else:
            paths.append(path)

    for path in sorted(set(paths)):
        violations = []

        try:
            with path.open("r") as file:
                text = file.read()
        except FileNotFoundError:
            console.print(
                format_error(
                    f"[red]Couldn't find file or directory[/] [bold]{path}[/]\n\n"
                    "Please check that the path is valid and try again."
                )
            )
            sys.exit(101)

        try:
            file_violations = check(text, ruleset)
        except SyntaxError as error:
            console.print(
                format_error(
                    (
                        f"[bold red]Couldn't parse the LookML in[/bold red] "
                        f"{format_path(path)}\n\nParser error: [red]{error}[/red]\n\n"
                        "The syntax of the LookML file might be invalid. "
                        "Double-check the LookML syntax at the line or "
                        "run the LookML validator in the Looker IDE.\n\n"
                        "If you find the LookML file [i]is[/i] valid, please submit an issue "
                        "with the file's contents to "
                        "[u blue link=https://github.com/joshtemple/lkml/issues/new]"
                        "https://github.com/joshtemple/lkml[/u blue link]"
                    )
                )
            )
            sys.exit(101)

        violations.extend(file_violations)
        lines = text.split("\n")

        if violations:
            failed = True
            console.rule(path.name, style="#9999ff")
            console.print()
        for violation in violations:
            code, title, rationale, line_number = violation
            console.print(f"[{code}] [bold red]{title}[/bold red]")
            console.print(f"{format_path(path)}:{line_number}")
            if args.show_rationale:
                console.rule(style="grey30")
                console.print(
                    Markdown("**Rationale:** " + rationale),
                    width=80,
                    highlight=False,
                    style="grey50",
                )
            console.rule(style="grey30")

            for i, n in enumerate(range(line_number - 1, line_number + 3)):
                if n <= 0:
                    continue
                # Don't print whitespace-only leading lines
                elif i == 0 and lines[n - 1].strip() == "":
                    continue
                elif n == line_number:
                    console.print(
                        f" {n:<4} [red]>[/red]| {escape(lines[n - 1])}",
                        highlight=False,
                        no_wrap=True,
                    )
                else:
                    console.print(
                        f" [dim]{n:<4}[/dim]  | [dim]{lines[n - 1]}[/dim]",
                        highlight=False,
                        no_wrap=True,
                    )
            console.print()

    if failed:
        sys.exit(100)


def rule_code(value, pattern=re.compile(r"[A-Z]+\d+")):
    if not pattern.match(value):
        console.print(
            format_error(
                f"[bold red]You specified an invalid rule code:[/] [bold]{value}[/]"
                "\n\nRule codes for --select and --ignore look like "
                "[bold]D105[/] or [bold]M112[/]. "
                "You can see all defined rule codes by running "
                "[code]lkmlstyle rules[/]."
                "\n\nIf the rule code looks right, perhaps you forgot to put "
                "--select or --ignore at the end "
                "of your command, after all file paths?"
            )
        )
        raise argparse.ArgumentTypeError("invalid format for rule code")
    return value


def main():
    parser = argparse.ArgumentParser(
        description=(
            "A flexible style checker for LookML. "
            "Run `lkmlstyle rules` to see all available rules."
        )
    )
    parser.add_argument(
        "path",
        nargs="+",
        type=pathlib.Path,
        help="path(s) to the file or directory to check",
    )
    parser.add_argument(
        "--ignore",
        nargs="+",
        metavar="CODE",
        required=False,
        type=rule_code,
        help="rule codes to exclude from checking, like 'D106' or 'M200'",
        default=[],
    )
    parser.add_argument(
        "--select",
        nargs="+",
        metavar="CODE",
        required=False,
        type=rule_code,
        help="only check the specified rule codes, like 'D106' or 'M200'",
        default=[],
    )
    parser.add_argument(
        "--show-rationale",
        action="store_true",
        help="for each violation, describe why the rule exists",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="show debugging logs",
        action="store_const",
        dest="loglevel",
        default=logging.WARNING,
        const=logging.DEBUG,
    )
    args = parser.parse_args()
    logs_handler.setLevel(args.loglevel)
    # This is a bit of a hack, but it's tough to get subparsers and positional args
    # to work together without adding something like `lkmlstyle check`.
    try:
        first_positional = str(args.path[0])
    except IndexError:
        pass

    if first_positional == "rules":
        print_rules_table()
    else:
        try:
            check_style(args)
        except LkmlstyleException as error:
            console.print(format_error(str(error)))
            sys.exit(error.code)
        except Exception:
            console.print(
                "[bold red]lkmlstyle encountered an unexpected issue.[/]"
                "\n\nWe're not sure what happened, but you can see the traceback below."
                "\n\n[dim]For support, please open an issue at "
                "[u blue link=https://github.com/spectacles-ci/lkmlstyle/]"
                "https://github.com/spectacles-ci/lkmlstyle/[/]\n"
            )
            raise


if __name__ == "__main__":
    main()
