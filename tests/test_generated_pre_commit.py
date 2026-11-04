import re
import subprocess
import sys
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run_generated_pre_commit(name, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("SKIP", raising=False)

    project = Path(
        cookiecutter(
            str(REPO_ROOT),
            no_input=True,
            extra_context={"project_name": name},
            output_dir=str(tmp_path),
            default_config={"replay_dir": str(tmp_path / "replay")},
        )
    )
    # The generation hook can continue after a failed workflow download.
    assert (project / ".github/workflows/check-news-item.yml").is_file()

    subprocess.run(
        ["git", "init", "-b", "pre-commit-test"], cwd=project, check=True
    )
    subprocess.run(["git", "add", "--all"], cwd=project, check=True)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pre_commit",
            "run",
            "--all-files",
            "--show-diff-on-failure",
            "--color",
            "never",
        ],
        cwd=project,
        capture_output=True,
        text=True,
    )
    output = result.stdout + result.stderr
    changed_files = subprocess.check_output(
        ["git", "diff", "--name-only"], cwd=project, text=True
    ).splitlines()

    return result.returncode, output, changed_files


@pytest.mark.parametrize(
    "name",
    [
        # C1: Generate a non-namespace package without a hyphen.
        # Expected: Pre-commit passes without changing any files.
        "mypackage",
        # C2: Generate a non-namespace package with a hyphen.
        # Expected: Pre-commit passes without changing any files.
        "my-package",
        # C3: Generate a namespace package without a hyphen.
        # Expected: Pre-commit passes without changing any files.
        "thisis.mypackage",
        # C4: Generate a namespace package with a hyphen in the package name.
        # Expected: Pre-commit passes without changing any files.
        "thisis.my-package",
    ],
)
def test_generated_package_passes_pre_commit(name, tmp_path, monkeypatch):
    actual_returncode, actual_output, actual_changed_files = (
        _run_generated_pre_commit(name, tmp_path, monkeypatch)
    )
    expected_returncode = 0
    expected_changed_files = []

    assert actual_returncode == expected_returncode, actual_output
    assert actual_changed_files == expected_changed_files, actual_output


def test_long_package_name_triggers_black_rewrite(tmp_path, monkeypatch):
    # C1: Generate a package with a long, hyphenated namespace and name.
    # Expected: Pre-commit fails only in Black, which rewrites conf.py.
    actual_returncode, actual_output, actual_changed_files = (
        _run_generated_pre_commit(
            "this-is-my-package.with-a-long-name", tmp_path, monkeypatch
        )
    )
    actual_failed_hooks = re.findall(
        r"^- hook id: (.+)$", actual_output, re.MULTILINE
    )
    actual_reports_rewrite = (
        "files were modified by this hook" in actual_output
    )
    expected_returncode = 1
    expected_failed_hooks = ["black"]
    expected_reports_rewrite = True
    expected_changed_files = ["docs/source/conf.py"]

    assert actual_returncode == expected_returncode, actual_output
    assert actual_failed_hooks == expected_failed_hooks, actual_output
    assert actual_reports_rewrite == expected_reports_rewrite, actual_output
    assert actual_changed_files == expected_changed_files, actual_output
