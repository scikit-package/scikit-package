|Icon| |title|_
===============

.. |title| replace:: {{ cookiecutter.conda_pypi_package_dist_name }}
.. _title: https://{{ cookiecutter.github_username_or_orgname }}.github.io/{{ cookiecutter.github_repo_name }}

.. |Icon| image:: https://avatars.githubusercontent.com/{{ cookiecutter.github_username_or_orgname }}
        :target: https://{{ cookiecutter.github_username_or_orgname }}.github.io/{{ cookiecutter.github_repo_name }}
        :height: 100px

|PyPI| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/actions/workflows/matrix-and-codecov.yml/badge.svg
        :target: https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/actions/workflows/matrix-and-codecov.yml

.. |Codecov| image:: https://codecov.io/gh/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/{{ cookiecutter.conda_pypi_package_dist_name }}
        :target: https://anaconda.org/conda-forge/{{ cookiecutter.conda_pypi_package_dist_name }}

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff
        :target: https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/pulls

.. |PyPI| image:: https://img.shields.io/pypi/v/{{ cookiecutter.conda_pypi_package_dist_name }}
        :target: https://pypi.org/project/{{ cookiecutter.conda_pypi_package_dist_name }}/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.conda_pypi_package_dist_name }}
        :target: https://pypi.org/project/{{ cookiecutter.conda_pypi_package_dist_name }}/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/issues

{{ cookiecutter.project_short_description }}

* LONGER DESCRIPTION HERE

For more information about the {{ cookiecutter.conda_pypi_package_dist_name }} library, please consult our `online documentation <https://{{ cookiecutter.github_username_or_orgname }}.github.io/{{ cookiecutter.github_repo_name }}>`_.

Citation
--------

If you use {{ cookiecutter.conda_pypi_package_dist_name }} in a scientific publication, we would like you to cite this package as

        {{ cookiecutter.conda_pypi_package_dist_name }} Package, https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``{{ cookiecutter.conda_pypi_package_dist_name }}_env`` ::

        conda create -n {{ cookiecutter.conda_pypi_package_dist_name }}_env {{ cookiecutter.conda_pypi_package_dist_name }}
        conda activate {{ cookiecutter.conda_pypi_package_dist_name }}_env

The output should print the latest version displayed on the badges above.

If the above does not work, you can use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``{{ cookiecutter.conda_pypi_package_dist_name }}_env`` environment, type ::

        pip install {{ cookiecutter.conda_pypi_package_dist_name }}

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/>`_. Once installed, ``cd`` into your ``{{ cookiecutter.github_repo_name }}`` directory
and run the following ::

        pip install .

This package also provides command-line utilities. To check the software has been installed correctly, type ::

        {{ cookiecutter.conda_pypi_package_dist_name }} --version

You can also type the following command to verify the installation. ::

        python -c "import {{ cookiecutter.package_dir_name }}; print({{ cookiecutter.package_dir_name }}.__version__)"


To view the basic usage and available commands, type ::

        {{ cookiecutter.conda_pypi_package_dist_name }} -h

Getting Started
---------------

You may consult our `online documentation <https://{{ cookiecutter.github_username_or_orgname }}.github.io/{{ cookiecutter.github_repo_name }}>`_ for tutorials and API references.

Support and Contribute
----------------------

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/issues>`_ and/or `submit a fix as a PR <https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/pulls>`_.

Feel free to fork the project and contribute. To install {{ cookiecutter.conda_pypi_package_dist_name }}
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contributing, please read our `Code of Conduct <https://github.com/{{ cookiecutter.github_username_or_orgname }}/{{ cookiecutter.github_repo_name }}/blob/main/CODE-OF-CONDUCT.rst>`_.

Contact
-------

For more information on {{ cookiecutter.conda_pypi_package_dist_name }} please visit the project `web-page <https://{{ cookiecutter.github_username_or_orgname }}.github.io/>`_ or email the maintainers ``{{ cookiecutter.maintainer_names | expand_to_str_with_email(cookiecutter.maintainer_emails)}}``.

Acknowledgements
----------------

``{{ cookiecutter.github_repo_name }}`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.
