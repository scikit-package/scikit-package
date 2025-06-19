import json
import os
import subprocess
from pathlib import Path

SKPKG_USER_CONFIG_FILE = "~/.skpkgrc"
try:
    USER_CONFIG_FILE = os.environ["SKPKG_CONFIG_FILE"]
except KeyError:
    USER_CONFIG_FILE = SKPKG_USER_CONFIG_FILE

SKPKG_PROJ_CONFIG_FILE = ".skpkgrc"

user_config_file = os.path.expandvars(SKPKG_USER_CONFIG_FILE)
user_config_path = Path(user_config_file).expanduser()
exist_user_config = user_config_path.exists()

proj_config_file = SKPKG_PROJ_CONFIG_FILE
proj_config_path = Path(SKPKG_PROJ_CONFIG_FILE)
exist_proj_config = proj_config_path.exists()


def read_skpkg_config(config_file):
    config_path = Path(config_file).expanduser()
    if not config_path.exists():
        raise FileNotFoundError(
            "scikit-packag configuration file ~/.skpkgrc is not found. "
            "Please try again after running 'touch ~/.skpkgrc'."
        )
    with config_path.open() as f:
        return json.load(f)


def get_extra_context():
    proj_config_dict = read_skpkg_config(proj_config_file)
    overwrite_context = [
        key + "=" + value
        for key, value in proj_config_dict.items()
        if not (value.startswith("[") and value.endswith("]"))
    ]
    return overwrite_context


def run(repo_url):
    run_cmd = ["cookiecutter", repo_url]

    if exist_proj_config:
        extra_context = get_extra_context()
        run_cmd.extend(extra_context)

    if exist_user_config:
        run_cmd.extend(["--config-file", str(user_config_path)])

    try:
        subprocess.run(
            run_cmd,
            check=True,
        )

    except subprocess.CalledProcessError as e:
        print(f"Failed to run scikit-package for the following reason: {e}")
