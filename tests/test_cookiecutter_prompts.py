import json
import subprocess
import sys
from pathlib import Path

import pytest
from click import ClickException
from cookiecutter.main import cookiecutter

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "answers, expected_last_prompt, expected_error",
    [
        # C1: Enter one author name for the two default author emails.
        # Expected: Stop after author_names, before asking about maintainers.
        (
            {"author_names": "Alice"},
            "author_names",
            "author_names and author_emails: "
            "The number of names and emails must be the same. "
            "Got 1 names and 2 emails.",
        ),
        # C2: Enter one maintainer name for the two default maintainer emails.
        # Expected: Stop after maintainer_emails, before asking for usernames.
        (
            {"maintainer_names": "Alice"},
            "maintainer_emails",
            "maintainer_names and maintainer_emails: "
            "The number of names and emails must be the same. "
            "Got 1 names and 2 emails.",
        ),
    ],
)
def test_invalid_answers_stop_cookiecutter_prompts(
    answers, expected_last_prompt, expected_error, tmp_path, mocker
):
    output_dir = tmp_path / "output"

    def answer(name, default, *_args):
        return answers.get(name, default)

    prompt = mocker.patch(
        "cookiecutter.prompt.read_user_variable", side_effect=answer
    )

    with pytest.raises(ClickException) as excinfo:
        cookiecutter(
            str(REPO_ROOT),
            output_dir=str(output_dir),
            default_config={"replay_dir": str(tmp_path / "replay")},
            accept_hooks=False,
        )

    actual_error = str(excinfo.value)
    actual_last_prompt = prompt.call_args.args[0]
    actual_output_created = output_dir.exists()
    expected_output_created = False
    assert actual_error == expected_error
    assert actual_last_prompt == expected_last_prompt
    assert actual_output_created == expected_output_created


def test_valid_answers_generate_project_settings(tmp_path):
    # C1: Accept the default author and maintainer contacts.
    # Expected: Generate the project and save only user settings.
    output_dir = tmp_path / "output"
    expected_project = output_dir / "diffpy.my-project"
    config = tmp_path / "cookiecutter.json"
    config.write_text(
        json.dumps({"replay_dir": str(tmp_path / "replay")}), encoding="utf-8"
    )
    # Keep raw Jinja template rendering outside pytest's coverage process.
    subprocess.run(
        [
            sys.executable,
            "-m",
            "cookiecutter",
            str(REPO_ROOT),
            "--no-input",
            "--output-dir",
            str(output_dir),
            "--config-file",
            str(config),
            "--accept-hooks",
            "no",
        ],
        cwd=tmp_path,
        check=True,
    )
    actual_projects = list(output_dir.iterdir())
    expected_projects = [expected_project]
    saved_settings = json.loads(
        (expected_project / "cookiecutter.json").read_text(encoding="utf-8")
    )
    actual_internal_settings = [
        key for key in saved_settings if key.startswith("_")
    ]
    expected_internal_settings = []
    assert actual_projects == expected_projects
    assert actual_internal_settings == expected_internal_settings
