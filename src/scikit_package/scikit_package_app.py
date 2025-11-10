import argparse
from argparse import ArgumentParser

from scikit_package.cli import add, create
from scikit_package.cli.build import api_doc
from scikit_package.cli.gh import broadcast_issue_to_repos
from scikit_package.cli.update import cf
from scikit_package.version import __version__

SKPKG_GITHUB_URL = "https://github.com/scikit-package/scikit-package"


def _add_subcommands(subparsers, commands, func, special_args={}):
    """Helper function to add subcommands to a parser."""
    for command, help_text in commands:
        parser_sub = subparsers.add_parser(
            command, help=help_text, epilog=help_text
        )
        if command in special_args:
            special_args[command](parser_sub)
        parser_sub.set_defaults(func=func, subcommand=command)


def _add_news_flags(p):
    """Helper function to add flags for `package add news/no-news`."""
    p.add_argument("-m", "--message", required=True, help="News content.")
    p.add_argument("-a", "--add", action="store_true", help="Added")
    p.add_argument("-c", "--change", action="store_true", help="Changed")
    p.add_argument("-d", "--deprecate", action="store_true", help="Deprecated")
    p.add_argument("-r", "--remove", action="store_true", help="Removed")
    p.add_argument("-f", "--fix", action="store_true", help="Fixed")
    p.add_argument("-s", "--security", action="store_true", help="Security")
    p.add_argument(
        "-n",
        "--no-news",
        action="store_true",
        help="Inform a brief reason why no news item is needed.",
    )


def _add_broadcast_args(p):
    p.add_argument(
        "issue_url",
        type=str,
        help="The URL of the issue to be broadcasted.",
    )
    p.add_argument(
        "group_name",
        type=str,
        help="The name of the group of repositories to broadcast to.",
    )
    p.add_argument(
        "--url-to-repo-info",
        type=str,
        help=(
            "The path or url to a JSON/YAML files "
            "containing repository info. When not provided, "
            "the command will search the current working directory first, "
            "then the directory specified by ~/.skpkgrc "
            "(default: none)."
        ),
    )
    p.add_argument(
        "--dry-run",
        choices=["y", "n"],
        default="y",
        help=(
            "Specify whether to run in dry-run mode (y/n). In this mode, the "
            "process is simulated and no issues are created in the target "
            "repositories (default: y)."
        ),
    )


def setup_subparsers(parser):
    # "create" subparser
    parser_create = parser.add_parser("create", help="Create a new package")
    subparsers_create = parser_create.add_subparsers(
        dest="subcommand", required=True
    )
    create_commands = [
        ("workspace", "Create a workspace package"),
        ("system", "Create a system package"),
        ("public", "Create a public package"),
        ("conda-forge", "Create a conda-forge recipe meta.yml file"),
        ("manuscript", "Create a LaTeX manuscript project"),
    ]
    _add_subcommands(subparsers_create, create_commands, create.package)
    # "add" subparser
    parser_add = parser.add_parser(
        "add", help="Add a new file like a news item"
    )
    subparsers_add = parser_add.add_subparsers(
        dest="subcommand", required=True
    )
    parser_news = subparsers_add.add_parser(
        "news",
        help="Add a news item under the news directory.",
        description=(
            "This command streamlines the process of writing news items.\n\n"
            "Add -a, -c, -d, -r, -f, or -s to specify the news type.\n"
            "If no news is necessary, add -n instead of any of the above.\n"
            "Then, add `-m <message>` to write the news message.\n\n"
            "Examples:\n"
            '  package add news --add -m "Add black pre-commit hook."\n'
            '  package add news -a -m "Support dark mode in UI."\n'
            '  package add no-news -m "Fix minor typo."'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    # "update" subparser
    parser_update = parser.add_parser(
        "update", help="Update an existing scikit-package standard package."
    )
    parser_update.set_defaults(func=cf.update)
    subparsers_update = parser_update.add_subparsers(
        dest="subcommand", required=False
    )
    update_commands = [
        (
            "conda-forge",
            "Update conda-forge recipe meta.yml file after release.",
        ),
    ]
    _add_subcommands(subparsers_update, update_commands, cf.update)
    # "build" subparser
    parser_build = parser.add_parser("build", help="Build API docs")
    subparsers_build = parser_build.add_subparsers(
        dest="subcommand", required=True
    )
    build_commands = [
        (
            "api-doc",
            "Generate API in docs/source/api for namespace import package.",
        ),
    ]
    _add_subcommands(subparsers_build, build_commands, api_doc.build)
    _add_news_flags(parser_news)
    parser_news.set_defaults(func=add.news_item, subcommand="news")

    parser_broadcast = parser.add_parser(
        "broadcast", help="Broadcast a issue to many GitHub repositories."
    )
    _add_broadcast_args(parser_broadcast)
    parser_broadcast.set_defaults(func=broadcast_issue_to_repos)


def main():
    """Entry point for the scikit-package CLI.

    Examples
    --------
    >>> package create workspace
    >>> package create system
    >>> package create public
    >>> package create manuscript
    >>> package create conda-forge
    >>> package add news -a -m "Add awesome news item."
    >>> package add news -n -m "Fix minor typo."
    >>> package update conda-forge
    >>> package update (Not implemented yet)
    """
    parser = ArgumentParser(
        description="Reduce effort for maintaining and developing packages."
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"scikit-package {__version__}",
        help="Show the version of scikit-package and exit.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    setup_subparsers(subparsers)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
