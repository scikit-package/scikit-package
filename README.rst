|Icon|
===============

.. |title| replace:: scikit-package
.. _title: https://scikit-package.github.io/scikit-package

.. |Icon| image:: https://raw.githubusercontent.com/scikit-package/scikit-package/main/img/logos/scikit-package-logo-text.png
        :target: https://scikit-package.github.io/scikit-package
        :height: 150px

|PyPI| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/scikit-package/scikit-package/actions/workflows/matrix-and-codecov.yml/badge.svg
        :target: https://github.com/scikit-package/scikit-package/actions/workflows/matrix-and-codecov.yml

.. |Codecov| image:: https://codecov.io/gh/scikit-package/scikit-package/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/scikit-package/scikit-package

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/scikit-package
        :target: https://anaconda.org/conda-forge/scikit-package

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff
        :target: https://github.com/scikit-package/scikit-package/pulls

.. |PyPI| image:: https://img.shields.io/pypi/v/scikit-package
        :target: https://pypi.org/project/scikit-package/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/scikit-package
        :target: https://pypi.org/project/scikit-package/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/scikit-package/scikit-package/issues

``scikit-package`` offers tools and practices for the scientific community to make better and more reusable Scientific Python packages and applications:

- We help scientists share scientific code to amplify research impact.

- We help scientists save time, allowing them to focus on writing scientific code.

- We offer best practices from the group's experience in developing scientific software.


Overview
--------

Here is an overview of the 5 levels of sharing code and the key features of ``scikit-package``:

.. image:: https://raw.githubusercontent.com/scikit-package/scikit-package/main/img/figures/scikit-package-overview-qr-code.png
    :alt: Diagram of 5 levels of sharing code with key features and scikit-package commands
    :width: 800px
    :align: center


Demo
----

Here is how you can use the ``package create public`` command to create a new Level 5 Python package called ``diffpy.my-project`` in just 1–2 minutes:

.. image:: https://raw.githubusercontent.com/scikit-package/scikit-package/main/img/gif/demo.gif
    :alt: Demonstration of creating a new Level 5 package with scikit-package
    :width: 800px
    :align: center

Getting started
---------------

Are you interested in using ``scikit-package``? Begin with the ``Getting Started`` page in our online documentation at https://scikit-package.github.io/scikit-package!

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``skpkg_env`` ::

        conda create -n skpkg_env scikit-package
        conda activate skpkg_env

To confirm that the installation was successful, type ::

        python -c "import scikit_package; print(scikit_package.__version__)"

The output should print the latest version displayed on the badges above.

If the above does not work, you can use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``skpkg_env`` environment, type ::

        pip install scikit-package

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/scikit-package/scikit-package/>`_. Once installed, ``cd`` into your ``scikit-package`` directory
and run the following ::

        pip install .

This package also provides command-line utilities. To conform the installation, type ::

        package --version

To view the basic usage and available commands, type ::

        package --h

How to cite ``scikit-package``
------------------------------

If you use ``scikit-package`` to standardize your Python software, we would like you to cite scikit-package:

  S. Lee, C. Myers, A. Yang, T. Zhang, Y. Xiao and S. J. L. Billinge, scikit-package: software packaging standards and roadmap for sharing reproducible scientific software, *Digital Discovery*, 2026. https://doi.org/10.1039/d6dd00121a

Support and Contribute
----------------------

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/scikit-package/scikit-package/issues>`_ and/or `submit a fix as a PR <https://github.com/scikit-package/scikit-package/pulls>`_.

Feel free to fork the project and contribute. To install scikit-package
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

Before contributing, please read our `Code of Conduct <https://github.com/scikit-package/scikit-package/blob/main/CODE-OF-CONDUCT.rst>`_.

Contact
-------

For more information on scikit-package please visit the project `web-page <https://scikit-package.github.io/scikit-package>`_ or email Simon Billinge at sbillinge@ucsb.edu.

Acknowledgements
----------------

``scikit-package`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.
