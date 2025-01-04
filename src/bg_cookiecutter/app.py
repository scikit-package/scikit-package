import subprocess
from argparse import ArgumentParser


def create():
    run_cookiecutter()


def update():
    run_cookiecutter()


def run_cookiecutter():
    try:
        subprocess.run(["cookiecutter", "https://github.com/Billingegroup/cookiecutter"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run cookiecutter for the following reason: {e}")


def setup_subparsers(parser):
    # Create subparser for the "create" command
    parser_create = parser.add_parser("create", help="Create a new package")
    parser_create.set_defaults(func=create)

    # Create subparser for the "update" command
    parser_update = parser.add_parser("update", help="Update an existing package")
    parser_update.set_defaults(func=update)


def main():
    """Entry point for the scikit-package CLI.

    Examples
    --------
    >>> package create
    >>> package update
    """
    parser = ArgumentParser(description="Manage package operations with cookiecutter.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    setup_subparsers(subparsers)

    args = parser.parse_args()
    args.func()


if __name__ == "__main__":
    main()
