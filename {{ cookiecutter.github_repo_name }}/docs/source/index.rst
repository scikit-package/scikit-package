#######
|title|
#######

.. |title| replace:: {{ cookiecutter.project_name }} documentation

``{{ cookiecutter.project_name }}`` - {{ cookiecutter.project_short_description }}

| Software version |release|
| Last updated |today|.

===============
Getting started
===============

Welcome to the ``{{ cookiecutter.project_name }}`` documentation!

To get started, please visit the :ref:`Getting started <getting-started>` page.

=======
Authors
=======

``{{ cookiecutter.project_name }}`` is developed by {{ cookiecutter.contributors }}. This project is maintained by {{ (cookiecutter.maintainers | split_contacts)[0] | join(', ') }}. For a detailed list of contributors see
https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/graphs/contributors.

============
Installation
============

See the `README <https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}#installation>`_
file included with the distribution.

================
Acknowledgements
================

``{{ cookiecutter.github_repo_name }}`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.

=================
Table of contents
=================
.. toctree::
   :maxdepth: 2

   getting-started
   Package API <api/{{ cookiecutter.package_dir_name }}>
   release
   license

=======
Indices
=======

* :ref:`genindex`
* :ref:`search`
