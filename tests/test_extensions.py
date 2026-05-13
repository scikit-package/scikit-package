import importlib
from pathlib import Path

import pytest
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
    "author_names, author_emails, expected_output",
    [
        # single author, expect return str with the form of
        #   a list with one dict
        (
            "Alice",
            "alice@email.com",
            ("[\n" "  {name='Alice', email='alice@email.com'},\n" "]"),
        ),
        # multiple authors, expect return str with the form of
        #   a list with multiple dicts
        (
            "Alice, Bob, Charlie",
            "alice@email.com, bob@email.com, charlie@email.com",
            (
                "[\n"
                "  {name='Alice', email='alice@email.com'},\n"
                "  {name='Bob', email='bob@email.com'},\n"
                "  {name='Charlie', email='charlie@email.com'},\n"
                "]"
            ),
        ),
    ],
)
def test_expand_to_dict_with_name(
    author_names, author_emails, expected_output
):

    template = extended_env.from_string(
        "{{ author_names | expand_to_dict_with_email(author_emails) }}"
    )
    actual_output = template.render(
        author_names=author_names, author_emails=author_emails
    )
    assert actual_output == expected_output


def test_expand_to_dict_with_name_bad():
    template = extended_env.from_string(
        "{{ author_names | expand_to_dict_with_email(author_emails) }}"
    )
    # mismatch number of names and emails, expect KeyError
    with pytest.raises(KeyError) as excinfo:
        template.render(
            author_names="Alice, Bob", author_emails="alice@email.com"
        )
    assert str(excinfo.value.args[0]) == (
        "The number of names and emails must be the same. "
        "Got 2 names and 1 emails."
    )


@pytest.mark.parametrize(
    "author_names, author_emails, expected_output",
    [
        # single author, expect return "Name(email)"
        ("Alice", "alice@email.com", "Alice(alice@email.com)"),
        # two authors, expect return "Name1(email1) and Name2(email2)"
        (
            "Alice, Bob",
            "alice@email.com, bob@email.com",
            "Alice(alice@email.com) and Bob(bob@email.com)",
        ),
        # multiple authors, expect return
        #   "Name1(email1), ..., and Name3(email3)"
        (
            "Alice, Bob, Charlie",
            "alice@email.com, bob@email.com, charlie@email.com",
            (
                "Alice(alice@email.com), Bob(bob@email.com), "
                "and Charlie(charlie@email.com)"
            ),
        ),
    ],
)
def test_expand_to_str_with_email(
    author_names, author_emails, expected_output
):
    template = extended_env.from_string(
        "{{ author_names | expand_to_str_with_email(author_emails) }}"
    )
    actual_output = template.render(
        author_names=author_names, author_emails=author_emails
    )
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
