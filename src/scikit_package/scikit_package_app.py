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
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-a", "--add", nargs="+", metavar="MESSAGE", help="Added news item."
    )
    group.add_argument(
        "-c",
        "--change",
        nargs="+",
        metavar="MESSAGE",
        help="Changed news item.",
    )
    group.add_argument(
        "-d",
        "--deprecate",
        nargs="+",
        metavar="MESSAGE",
        help="Deprecated news item.",
    )
    group.add_argument(
        "-r",
        "--remove",
        nargs="+",
        metavar="MESSAGE",
        help="Removed news item.",
    )
    group.add_argument(
        "-f", "--fix", nargs="+", metavar="MESSAGE", help="Fixed news item."
    )
    group.add_argument(
        "-s",
        "--security",
        nargs="+",
        metavar="MESSAGE",
        help="Security news item.",
    )
    group.add_argument(
        "-n",
        "--no-news",
        nargs="+",
        metavar="MESSAGE",
        help="Inform a brief reason why no news item is needed.",
    )


def _add_broadcast_args(p):
    p.add_argument(
        "issue_url",
        type=str,
        help="The URL of the issue to be broadcast.",
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
        "add",
        help=(
            "Add a new file like a news item or generate a "
            "deprecation docstring."
        ),
    )
    subparsers_add = parser_add.add_subparsers(
        dest="subcommand", required=True
    )
    parser_news = subparsers_add.add_parser(
        "news",
        help="Add a news item under the news directory.",
        description=(
            "This command streamlines the process of writing news items.\n\n"
            "Add -a, -c, -d, -r, -f, or -s to specify the news type followed "
            "by your message.\n"
            "If no news is necessary, add -n instead of any of the above.\n"
            "Examples:\n"
            '  package add news -a "Support dark mode in UI."\n'
            '  package add news -n "Fix minor typo."'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser_deprecation = subparsers_add.add_parser(
        "deprecation",
        help="Print a standardized docstring for deprecated functions.",
        description=(
            "Generate a standardized deprecation docstring for copy-pasting "
            "into deprecated functions or classes.\n\n"
            "Examples:\n"
            "  package add deprecation new_func 4.0.0\n"
            "  package add deprecation new_func 4.0.0 --new-base diffpy.foo"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser_deprecation.add_argument(
        "new_name",
        help="Name of the replacement function or class.",
    )

    parser_deprecation.add_argument(
        "removal_version",
        help="Version when the deprecated item will be removed (e.g. 4.0.0).",
    )

    parser_deprecation.add_argument(
        "-n",
        "--new-base",
        default=None,
        help='Base module if necessary (e.g. "diffpy.foo").',
    )
    parser_deprecation.set_defaults(func=add.print_deprecation_docstring)
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
        "broadcast",
        help="Broadcast an issue to a list of GitHub repositories.",
        description=(
            "The issue is specified by its URL, and the repositories are "
            "specified by custom options defined in groups.json and "
            "repos.json. If --url-to-repo-info is provided, "
            "scikit-package will attempt to locate these files in the "
            "specified GitHub repository. Otherwise, it will look for "
            "them in the current working directory and in the "
            "url_to_repo_info entry of ~/.skpkgrc. "
            "See https://scikit-package.github.io/scikit-package/"
            "additional-functionalities/broadcast.html for details.\n"
            "Example of repos.json:\n"
            "{\n"
            '    "<repo1>": "https://github.come/<org-name>/<repo1>",\n'
            '    "<repo2>": "https://github.come/<org-name>/<repo2>",\n'
            '    "<repo3>": "https://github.come/<org-name>/<repo3>",\n'
            '    "<repo4>": "https://github.come/<org-name>/<repo4>"\n'
            "}\n"
            "Example of groups.json:\n"
            "{\n"
            '    "even_group" : ["<repo2>", "<repo4>"],\n'
            '    "odd_group" : ["<repo1>", "<repo3>"]\n'
            "}\n"
            "Example of usage:\n"
            "    package broadcast <issue-url> even_group\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
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
