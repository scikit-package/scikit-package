from click import ClickException
from jinja2.ext import Extension


def _split_contacts(names, emails):
    names = names.split(",")
    emails = emails.split(",")
    if len(names) != len(emails):
        raise KeyError(
            "The number of names and emails must be the same. "
            f"Got {len(names)} names and {len(emails)} emails."
        )
    return names, emails


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
        environment.filters["validate_contact_pair"] = (
            self.validate_contact_pair
        )

    def expand_to_dict_with_email(self, names, emails):
        """Expand names and emails to a list of dicts."""
        names, emails = _split_contacts(names, emails)
        people_contact_info_Extension = ""
        for n, e in zip(names, emails):
            people_contact_info_Extension += (
                f"  {{name='{n.strip()}', email='{e.strip()}'}},\n"
            )
        people_contact_info_Extension = (
            "[\n" + people_contact_info_Extension + "]"
        )
        return people_contact_info_Extension

    def expand_to_str_with_email(self, names, emails):
        """Expand names with emails in parentheses."""
        names, emails = _split_contacts(names, emails)
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

    def validate_contact_pair(self, names, emails, role):
        """Validate a contact pair during Cookiecutter prompting."""
        try:
            _split_contacts(names, emails)
        except KeyError as error:
            raise ClickException(
                f"{role}_names and {role}_emails: {error.args[0]}"
            ) from None
        return ""
