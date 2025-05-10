import os
import subprocess
from argparse import ArgumentParser

SKPKG_GITHUB_URL = "https://github.com/Billingegroup/scikit-package"
USER_CONFIG_FILE = "~/.skpkgrc"


def create(package_type):
    if package_type == "workspace":
        run_cookiecutter(f"{SKPKG_GITHUB_URL}-workspace")
    elif package_type == "system":
        run_cookiecutter(f"{SKPKG_GITHUB_URL}-system")
    elif package_type == "public":
        run_cookiecutter(SKPKG_GITHUB_URL)
    elif package_type == "conda-forge":
        run_cookiecutter(f"{SKPKG_GITHUB_URL}-conda-forge")


def update():
    # FIXME: Implement the update command.
    # As of now it does the same as the create command.
    run_cookiecutter(SKPKG_GITHUB_URL)


def run_cookiecutter(repo_url):
    try:
        config_file = os.environ["SKPKG_CONFIG_FILE"]
    except KeyError:
        config_file = USER_CONFIG_FILE
    config_file = os.path.expandvars(config_file)
    config_file = os.path.expanduser(config_file)
    if os.path.exists(path):
        try:
            subprocess.run(
                [
                    "cookiecutter",
                    repo_url,
                    "--config-file",
                    config_file,
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print(
                f"Failed to run scikit-package for the following reason: {e}"
            )
    else:
        try:
            subprocess.run(
                [
                    "cookiecutter",
                    repo_url,
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print(
                f"Failed to run scikit-package for the following reason: {e}"
            )


def setup_subparsers(parser):
    # Create "create" subparser
    parser_create = parser.add_parser("create", help="Create a new package")

    # Add subcommands under "create" for different
    sub_create = parser_create.add_subparsers(
        dest="package_type", required=True
    )

    # "workspace" subcommand
    parser_create_workspace = sub_create.add_parser(
        "workspace", help="Create a workspace package"
    )
    parser_create_workspace.set_defaults(func=create, package_type="workspace")

    # "system" subcommand
    parser_create_system = sub_create.add_parser(
        "system", help="Create a system package"
    )
    parser_create_system.set_defaults(func=create, package_type="system")

    # "public" subcommand
    parser_create_public = sub_create.add_parser(
        "public", help="Create a public package"
    )
    parser_create_public.set_defaults(func=create, package_type="public")

    # "conda-forge" subcommand
    parser_create_conda_forge = sub_create.add_parser(
        "conda-forge", help="Create a conda-forge recipe meta.yml file"
    )
    parser_create_conda_forge.set_defaults(
        func=create, package_type="conda-forge"
    )

    # Create "update" subparser
    parser_update = parser.add_parser(
        "update", help="Update an existing package"
    )
    parser_update.set_defaults(func=update)


def main():
    """Entry point for the scikit-package CLI.

    Examples
    --------
    >>> package create workspace
    >>> package create system
    >>> package create public
    >>> package update
    """

    parser = ArgumentParser(
        description="Manage package operations with scikit-package."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    setup_subparsers(subparsers)
    args = parser.parse_args()
    args.func(args.package_type)


if __name__ == "__main__":
    main()
