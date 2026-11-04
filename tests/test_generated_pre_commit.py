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
    ["mypackage", "my-package", "thisis.mypackage", "thisis.my-package"],
)
def test_generated_package_passes_pre_commit(name, tmp_path, monkeypatch):
    returncode, output, changed_files = _run_generated_pre_commit(
        name, tmp_path, monkeypatch
    )
    assert returncode == 0, output
    assert not changed_files, output


def test_long_package_name_triggers_black_rewrite(tmp_path, monkeypatch):
    returncode, output, changed_files = _run_generated_pre_commit(
        "this-is-my-package.with-a-long-name", tmp_path, monkeypatch
    )
    assert returncode == 1, output
    assert re.findall(r"^- hook id: (.+)$", output, re.MULTILINE) == [
        "black"
    ], output
    assert "files were modified by this hook" in output, output
    assert changed_files == ["docs/source/conf.py"], output
