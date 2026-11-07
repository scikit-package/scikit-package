import json
import re

from click import ClickException
from jinja2.ext import Extension


def _split_contacts(contacts):
    pairs = []
    for entry in contacts.split(";"):
        pair = re.fullmatch(
            r"\s*([^<>]+?)\s*<([^<>\s@]+@[^<>\s@]+)>\s*", entry
        )
        if pair is None or not pair[1].strip():
            raise KeyError("Use Name <email> pairs separated by semicolons.")
        pairs.append((pair[1].strip(), pair[2]))
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

    def expand_to_dict_with_email(self, contacts):
        """Expand names and emails to a list of dicts."""
        names, emails = _split_contacts(contacts)
        people_contact_info_Extension = ""
        for n, e in zip(names, emails):
            n = json.dumps(n, ensure_ascii=False)
            e = json.dumps(e, ensure_ascii=False)
            people_contact_info_Extension += f"  {{name={n}, email={e}}},\n"
        people_contact_info_Extension = (
            "[\n" + people_contact_info_Extension + "]"
        )
        return people_contact_info_Extension

    def expand_to_str_with_email(self, contacts):
        """Expand names with emails in parentheses."""
        names, emails = _split_contacts(contacts)
        people_contact_info_Extension = (
            f"{names[0].strip()}({emails[0].strip()})"
        )
        if len(names) == 2:
            people_contact_info_Extension += (
                f" and {names[1].strip()}({emails[1].strip()})"
            )
            return people_contact_info_Extension

        # for 3 or more names
        for i in range(1, len(names)):
            if i != len(names) - 1:
                people_contact_info_Extension += (
                    f", {names[i].strip()}({emails[i].strip()})"
                )
            else:
                people_contact_info_Extension += (
                    f", and {names[i].strip()}({emails[i].strip()})"
                )

        people_contact_info_Extension = people_contact_info_Extension
        return people_contact_info_Extension

    def list_in_str(self, items):
        """Convert a list of items to a comma-separated string with
        'and' before the last item."""
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
