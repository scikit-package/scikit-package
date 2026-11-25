import json
import subprocess
import sys
import tomllib
from pathlib import Path

import pytest
from click import ClickException
from cookiecutter.main import cookiecutter

from scikit_package.utils.cookie import SCHEMA_KEY

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "answers, expected_last_prompt, expected_error",
    [
        # C1: Enter an author with an unmatched email bracket.
        # Expected: Stop at authors, before asking about maintainers.
        pytest.param(
            {"authors": "Alice <alice@example.org"},
            "authors",
            "authors: Use Name, Name email, or Name <email>, "
            "separated by semicolons.",
            id="unclosed-author-email",
        ),
        # C2: Enter a maintainer with an incomplete email address.
        # Expected: Stop at maintainers, before asking for usernames.
        pytest.param(
            {"maintainers": "Alice alice@"},
            "maintainers",
            "maintainers: Use Name, Name email, or Name <email>, "
            "separated by semicolons.",
            id="incomplete-maintainer-email",
        ),
        # C3: Enter multiple GitHub usernames.
        # Expected: Raise ClickException at the release username prompt,
        # before asking for the project name or creating an output directory.
        pytest.param(
            {"authorized_maintainer_github_username": "alice, bob"},
            "authorized_maintainer_github_username",
            "authorized_maintainer_github_username: Enter exactly "
            "one GitHub username, without @, spaces, commas, "
            "or semicolons.",
            id="multiple-release-usernames",
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


@pytest.mark.parametrize(
    "contacts, expected_people, expected_enforcement",
    [
        # C1: Type emails without brackets, then press Enter for maintainers.
        # Expected: Reuse both contacts with emails and save the supplied
        # authorized GitHub username.
        pytest.param(
            "Alice alice@example.org; Bob bob@example.org",
            [
                {"name": "Alice", "email": "alice@example.org"},
                {"name": "Bob", "email": "bob@example.org"},
            ],
            "enforcement at alice@example.org, bob@example.org.",
            id="plain-emails",
        ),
        # C2: Paste a bracketed email and omit the other person's email.
        # Expected: Reuse both contacts, include only the available email,
        # and save the supplied authorized GitHub username.
        pytest.param(
            "Alice <alice@example.org>; Bob",
            [{"name": "Alice", "email": "alice@example.org"}, {"name": "Bob"}],
            "enforcement at alice@example.org.",
            id="mixed-optional-emails",
        ),
        # C3: Enter names only, then press Enter for maintainers.
        # Expected: Save both names without emails and the supplied authorized
        # GitHub username, without an empty contact-email clause.
        pytest.param(
            "Alice; Bob",
            [{"name": "Alice"}, {"name": "Bob"}],
            "enforcement. All complaints",
            id="names-only",
        ),
    ],
)
def test_valid_answers_generate_project_settings(
    contacts, expected_people, expected_enforcement, tmp_path
):
    output_dir = tmp_path / "output"
    expected_project = output_dir / "diffpy.my-project"
    expected_username = "release-user"
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
            "--output-dir",
            str(output_dir),
            "--config-file",
            str(config),
            "--accept-hooks",
            "no",
        ],
        cwd=tmp_path,
        check=True,
        input=f"{contacts}\n\n{expected_username}\n" + "\n" * 14,
        text=True,
    )
    actual_projects = list(output_dir.iterdir())
    expected_projects = [expected_project]
    saved_settings = json.loads(
        (expected_project / "cookiecutter.json").read_text(encoding="utf-8")
    )
    actual_internal_settings = [
        key for key in saved_settings if key.startswith("_")
    ]
    template_settings = json.loads(
        (REPO_ROOT / "cookiecutter.json").read_text(encoding="utf-8")
    )

    expected_internal_settings = [SCHEMA_KEY]
    expected_schema_version = template_settings[SCHEMA_KEY]
    actual_schema_version = saved_settings[SCHEMA_KEY]

    assert actual_schema_version == expected_schema_version
    assert actual_projects == expected_projects
    assert actual_internal_settings == expected_internal_settings
    assert saved_settings["authors"] == contacts
    assert saved_settings["maintainers"] == contacts
    actual_username = saved_settings["authorized_maintainer_github_username"]
    assert actual_username == expected_username
    metadata = tomllib.loads(
        (expected_project / "pyproject.toml").read_text(encoding="utf-8")
    )["project"]
    assert metadata["authors"] == expected_people
    assert metadata["maintainers"] == expected_people
    actual_enforcement = " ".join(
        (expected_project / "CODE-OF-CONDUCT.rst").read_text().split()
    )
    assert expected_enforcement in actual_enforcement
