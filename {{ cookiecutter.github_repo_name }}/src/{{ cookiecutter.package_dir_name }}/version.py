#!/usr/bin/env python
##############################################################################
#
# (c) {% now 'utc', '%Y' %} {{ cookiecutter.license_holders }}.
# All rights reserved.
#
# File coded by: {{ cookiecutter.__contributors_str }}.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/graphs/contributors  # noqa: E501
#
# See LICENSE.rst for license information.
#
##############################################################################
"""Definition of __version__."""

#  We do not use the other three variables, but can be added back if needed.
#  __all__ = ["__date__", "__git_commit__", "__timestamp__", "__version__"]

# obtain version information
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{ cookiecutter.package_dir_name }}")
except PackageNotFoundError:
    __version__ = "unknown"
