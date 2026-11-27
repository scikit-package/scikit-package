import json
import re

from click import ClickException
from jinja2.ext import Extension


def _split_contacts(contacts):
    pairs = []
    for entry in contacts.split(";"):
        pair = re.fullmatch(
            r"\s*([^<>@]+?)(?:\s*<([^<>\s@]+@[^<>\s@]+)>"
            r"|\s+([^<>\s@]+@[^<>\s@]+))?\s*",
            entry,
        )
        if pair is None or not pair[1].strip():
            raise KeyError(
                "Use Name, Name email, or Name <email>, "
                "separated by semicolons."
            )
        pairs.append((pair[1].strip(), pair[2] or pair[3]))
    return tuple(zip(*pairs))


class people_contact_info_Extension(Extension):
    def __init__(self, environment):
        super(people_contact_info_Extension, self).__init__(environment)
        environment.filters["expand_to_dict_with_email"] = (
            self.expand_to_dict_with_email
        )
        environment.filters["expand_to_str_with_email"] = (
            self.expand_to_str_with_email
        )
        environment.filters["list_in_str"] = self.list_in_str
        environment.filters["split_contacts"] = _split_contacts
        environment.filters["validate_contact_pair"] = (
            self.validate_contact_pair
        )
        environment.filters["validate_single_github_username"] = (
            self.validate_single_github_username
        )

    def expand_to_dict_with_email(self, contacts):
        """Expand names and emails to a list of dicts."""
        names, emails = _split_contacts(contacts)
        people_contact_info_Extension = ""
        for n, e in zip(names, emails):
            n = json.dumps(n, ensure_ascii=False)
            email_field = (
                f", email={json.dumps(e, ensure_ascii=False)}" if e else ""
            )
            people_contact_info_Extension += f"  {{name={n}{email_field}}},\n"
        people_contact_info_Extension = (
            "[\n" + people_contact_info_Extension + "]"
        )
        return people_contact_info_Extension

    def expand_to_str_with_email(self, contacts):
        """Expand names with emails in parentheses."""
        names, emails = _split_contacts(contacts)
        return self.list_in_str(
            [
                f"{name}({email})" if email else name
                for name, email in zip(names, emails)
            ]
        )

    def list_in_str(self, items):
        """Convert a list of items to a comma-separated string with
        'and' before the last item."""
        if isinstance(items, str):
            items = [item.strip() for item in items.split(",")]
        if len(items) == 1:
            return items[0]
        if len(items) == 2:
            return " and ".join(items)
        return ", ".join(items[:-1]) + ", and " + items[-1]

    def validate_contact_pair(self, contacts, role):
        """Validate a contact pair during Cookiecutter prompting."""
        try:
            _split_contacts(contacts)
        except KeyError as error:
            raise ClickException(f"{role}: {error.args[0]}") from None
        return ""

    def validate_single_github_username(self, username):
        """Validate a single GitHub login during prompting."""
        if not isinstance(username, str) or not re.fullmatch(
            r"[A-Za-z0-9_-]+", username
        ):
            raise ClickException(
                "authorized_maintainer_github_username: Enter exactly "
                "one GitHub username, without @, spaces, commas, "
                "or semicolons."
            )
        return ""
