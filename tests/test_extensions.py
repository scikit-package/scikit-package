import importlib
import tomllib
from pathlib import Path

import pytest
from click import ClickException
from jinja2 import Environment

spec = importlib.util.spec_from_file_location(
    "local_extensions",
    Path(__file__).parents[1] / "hooks" / "local_extensions.py",
)
local_extensions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(local_extensions)
extended_env = Environment(
    extensions=[local_extensions.people_contact_info_Extension]
)


@pytest.mark.parametrize(
    "contacts, expected_output",
    [
        # single author, expect return str with the form of
        #   a list with one dict
        (
            "Alice <alice@email.com>",
            ("[\n" "  {name='Alice', email='alice@email.com'},\n" "]"),
        ),
        # multiple authors, expect return str with the form of
        #   a list with multiple dicts
        (
            "Alice <alice@email.com>; Bob <bob@email.com>; "
            "Charlie <charlie@email.com>",
            (
                "[\n"
                "  {name='Alice', email='alice@email.com'},\n"
                "  {name='Bob', email='bob@email.com'},\n"
                "  {name='Charlie', email='charlie@email.com'},\n"
                "]"
            ),
        ),
        # C3: Type an email without angle brackets.
        # Expected: Generate the same name/email metadata.
        (
            "Alice alice@email.com",
            "[{name='Alice', email='alice@email.com'}]",
        ),
        # C4: Omit one email and include punctuation in the name.
        # Expected: Omit that email field and preserve both contacts.
        (
            "Doe, Jane; Bob bob@email.com",
            "[{name='Doe, Jane'}, {name='Bob', email='bob@email.com'}]",
        ),
    ],
)
def test_expand_to_dict_with_name(contacts, expected_output):

    template = extended_env.from_string(
        "{{ contacts | expand_to_dict_with_email }}"
    )
    actual_output = template.render(contacts=contacts)
    assert tomllib.loads("people = " + actual_output) == tomllib.loads(
        "people = " + expected_output
    )


@pytest.mark.parametrize(
    "contacts",
    [
        # C1: Unclosed bracket. Expected: Reject the malformed email.
        "Alice <alice@email.com",
        # C2: Unmatched closing bracket. Expected: Reject the malformed email.
        "Alice alice@email.com>",
        # C3: No name. Expected: Still require a name.
        "alice@email.com",
        # C4: Missing separator. Expected: Reject multiple emails in one entry.
        "Alice alice@email.com Bob bob@email.com",
        # C5: Empty entry. Expected: Still require a name.
        "",
    ],
)
def test_expand_to_dict_with_name_bad(contacts):
    template = extended_env.from_string(
        "{{ contacts | expand_to_dict_with_email }}"
    )
    with pytest.raises(KeyError) as excinfo:
        template.render(contacts=contacts)
    assert str(excinfo.value.args[0]) == (
        "Use Name, Name email, or Name <email>, separated by semicolons."
    )


@pytest.mark.parametrize(
    "contacts, expected_output",
    [
        # single author, expect return "Name(email)"
        ("Alice <alice@email.com>", "Alice(alice@email.com)"),
        # two authors, expect return "Name1(email1) and Name2(email2)"
        (
            "Alice <alice@email.com>; Bob <bob@email.com>",
            "Alice(alice@email.com) and Bob(bob@email.com)",
        ),
        # multiple authors, expect return
        #   "Name1(email1), ..., and Name3(email3)"
        (
            "Alice <alice@email.com>; Bob <bob@email.com>; "
            "Charlie <charlie@email.com>",
            (
                "Alice(alice@email.com), Bob(bob@email.com), "
                "and Charlie(charlie@email.com)"
            ),
        ),
        # C4: Mix names with and without emails.
        # Expected: Do not add empty parentheses for missing emails.
        ("Alice; Bob bob@email.com", "Alice and Bob(bob@email.com)"),
        # C5: A name contains a comma.
        # Expected: Preserve it as one person's name.
        ("Doe, Jane", "Doe, Jane"),
    ],
)
def test_expand_to_str_with_email(contacts, expected_output):
    template = extended_env.from_string(
        "{{ contacts | expand_to_str_with_email }}"
    )
    actual_output = template.render(contacts=contacts)
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "author_names, expected_output",
    [
        # single author, expect return the name
        ("Alice", "Alice"),
        # two authors, expect return "Name1 and Name2"
        ("Alice, Bob", "Alice and Bob"),
        # multiple authors, expect return "Name1, Name2, and Name3"
        ("Alice, Bob, Charlie", "Alice, Bob, and Charlie"),
    ],
)
def test_list_in_str(author_names, expected_output):
    template = extended_env.from_string("{{ author_names | list_in_str }}")
    actual_output = template.render(author_names=author_names)
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "username",
    [
        # C1: A single personal username.
        "alice",
        # C2: A single username containing a hyphen.
        "release-user",
        # C3: A managed user's login can include an underscore.
        "mona-cat_octo",
    ],
)
def test_validate_single_github_username(username):
    # Expected: Accept one login without adding text to the context.
    template = extended_env.from_string(
        "{{ username | validate_single_github_username }}"
    )
    actual_output = template.render(username=username)
    expected_output = ""
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "username",
    [
        # C1: Multiple usernames separated by a comma.
        "alice, bob",
        # C2: Multiple usernames separated by a semicolon.
        "alice;bob",
        # C3: Multiple usernames separated by whitespace.
        "alice bob",
        # C4: A pasted mention rather than a bare username.
        "@alice",
        # C5: A profile URL rather than a bare username.
        "https://github.com/alice",
        # C6: No release username supplied.
        "",
        # C7: A list instead of a single username.
        ["alice", "bob"],
    ],
)
def test_validate_single_github_username_bad(username):
    # Expected: Reject the value with guidance for entering one login.
    template = extended_env.from_string(
        "{{ username | validate_single_github_username }}"
    )
    with pytest.raises(ClickException) as excinfo:
        template.render(username=username)
    actual_error = str(excinfo.value)
    expected_error = (
        "authorized_maintainer_github_username: Enter exactly "
        "one GitHub username, without @, spaces, commas, or semicolons."
    )
    assert actual_error == expected_error
