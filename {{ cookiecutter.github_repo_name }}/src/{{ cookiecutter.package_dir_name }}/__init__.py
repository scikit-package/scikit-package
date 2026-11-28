#!/usr/bin/env python
##############################################################################
#
# (c) {% now 'utc', '%Y' %} {{ cookiecutter.license_holders }}.
# All rights reserved.
#
# File coded by: {{ cookiecutter.__contributors_str }}.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
"""{{ cookiecutter.project_short_description }}"""

# package version
from {{cookiecutter.package_dir_name}}.version import __version__  # noqa

# silence the pyflakes syntax checker
assert __version__ or True

# End of file
