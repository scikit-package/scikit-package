import os
import shutil

from diffpy.utils._deprecator import build_deprecation_docstring

from scikit_package.utils import auth, io

NEWS_HEADER_MAP = {
    "add": "**Added:**",
    "change": "**Changed:**",
    "deprecate": "**Deprecated:**",
    "remove": "**Removed:**",
    "fix": "**Fixed:**",
    "security": "**Security:**",
}

TEMPLATE_PATH = "news/TEMPLATE.rst"
NEWS_DIR = "news"


def _check_news_file_exists(branch_name):
    """Ensure <branch-name>.rst file exists, otherwise create it."""
    path = os.path.join(NEWS_DIR, f"{branch_name}.rst")
    if not os.path.exists(path):
        shutil.copy(TEMPLATE_PATH, path)
    return path


def _insert_news_item(lines, flags, message):
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        new_lines.append(line)
        for flag in flags:
            if stripped == NEWS_HEADER_MAP[flag]:
                j = i + 1
                while j < len(lines) and lines[j].strip() in (
                    "",
                    "* <news item>",
                ):
                    j += 1
                new_lines.append("\n")
                new_lines.append(f"* {message}\n")
                if j >= len(lines) or lines[j].strip().startswith("**"):
                    new_lines.append("\n")
                i = j - 1
        i += 1
    return new_lines


def _insert_no_news_item(lines, message):
    replaced = False
    new_lines = []

    for line in lines:
        if not replaced and line.strip() == "* <news item>":
            new_lines.append(f"* No news added: {message}\n")
            replaced = True
        else:
            new_lines.append(line)
    return new_lines


def news_item(args):
    """Handle adding a news item or no news item."""
    message = args.message
    # Directly match NEWS_HEADER_MAP keys to argument attributes
    flags_used = [flag for flag in NEWS_HEADER_MAP if getattr(args, flag)]
    branch = auth.get_current_branch()
    path = _check_news_file_exists(branch)
    lines = io.read_file(path)
    if not flags_used:
        updated = _insert_no_news_item(lines, message)
    else:
        updated = _insert_news_item(lines, flags_used, message)
    io.write_file(path, updated)
    print(f"Done! Appended news item to {path}")


def print_deprecation_docstring(args):
    """Generate a standardized docstring for deprecated functions."""
    build_deprecation_docstring(
        new_name=args.new_name,
        removal_version=args.removal_version,
        new_base=args.new_base,
    )
