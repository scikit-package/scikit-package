.. _example-1:

Example 1. Create your first Level 4 package
=============================================

In this example, we assume **Mr Neutron** previously initiated a project called ``diffraction-utils`` using ``scikit-package`` Level 3 and developed a shared class called ``DiffractionObject``. This ``DiffractionObject`` is used in code analyzing various diffraction data sourced from x-ray, neutron, and electron instruments. This class is written in a module called ``diffraction_objects.py`` which is reused in Python scripts in the ``scattering`` sub-project folder. **Mr Neutron**'s folder structure looks like the following:

.. code-block:: text

    somewhere/
        |-- on/
            |-- my/
                |-- computer/
                    |-- diffraction-utils/
                        |-- README.md
                        |-- diffraction_objects.py
                        |-- scattering/
                            |-- __init__.py
                            |-- neutron.py
                            |-- xray.py
                            |-- electron.py


Since the project is a data analysis project, **Mr Neutron** followed common practice to place this ``diffraction-utils`` folder near the location of the data. Since **Mr Neutron** wants to create a package that is shared across many different projects, it is recommended to place the package in a common directory where he keeps all his reused system-wide packages. This could be called anything, but following standard practice he called this directory dev (roughly short for code-development-area) that he placed in his home directory. In the example, **Mr Neutron** is working on Windows but using a bash terminal from the “Git for Windows”(https://git-scm.com/downloads/win) software. This is a recommended setup for Windows users.

Create a new empty project with ``scikit-package``
--------------------------------------------------

Using the bash terminal, **Mr Neutron** navigates to his ``dev`` directory, activates the Conda environment where ``scikit-package`` is installed, and creates an empty **Level 4 system** project by typing these commands:

.. code-block:: bash

    $ cd ~/dev
    $ conda activate skpkg-env
    $ package create system

**Mr Neutron** enters the following values to the questions ``scikit-package`` prompts (no response indicates he hit enter to accept the default value in parentheses):

.. code-block:: bash

    [1/6] project_name (my-project): diffraction-utils
    [2/6] github_username_or_orgname (billingegroup): mrneutron44
    [3/6] github_repo_name (my-project): diffraction-utils
    [4/6] conda_pypi_package_dist_name (diffraction-utils):
    [5/6] package_dir_name (diffraction_utils):
    [6/6] contributors (Sangjoon Lee, Simon Billinge): Mr Neutron

**Mr Neutron** now sees the following empty package created on the hard-drive:

.. code-block:: bash

    ~/dev/
        |-- diffraction-utils/
            |-- .flake8
            |-- .github
                |-- ISSUE_TEMPLATE
                    |-- bug_feature.md
                |-- workflows
                    |-- tests-on-pr.yml
            |-- .gitignore
            |-- .pre-commit-config.yaml
            |-- LICENSE.rst
            |-- README.md
            |-- requirements
                |-- conda.txt
                |-- pip.txt
                |-- tests.txt
            |-- src/
                |-- diffraction_utils/
                    |-- __init__.py
                    |-- functions.py
            |-- tests
                |-- test_functions.py

The created files are described in detail in the ``scikit-package`` in :ref:`level-4-tutorial`.

Copy files to the new project directory
---------------------------------------

At this point, ``scikit-package`` simply created an empty package with files appropriately named based on **Mr Neutron**'s responses. Next **Mr Neutron** copies his code, the ``diffraction_objects.py`` file into the ``diffraction_utils`` folder. He can do this using Windows explorer, but chooses to do it in a terminalby typing the following commands:

.. code-block:: bash

    $ cd ~/dev/diffraction-utils/diffraction_utils
    $ cp somewhere/on/my/computer/diffraction-utils/diffraction_objects.py .

**Mr Neutron** made sure to type the small dot (“.”) at the end of the last command.

Install package and test
------------------------

There are still a few quick steps that **Mr Neutron** needs to complete before the code is available everywhere in his computer.

First, **Mr Neutron** needs to specify the package dependencies within the ``conda.txt`` and ``pip.txt`` files in the requirements folder. In this example, **Mr Neutron** enters numpy and matplotlib-base in ``conda.txt`` and ``numpy`` and ``matplotlib`` in ``pip.txt``, one per line. After he has done this the contents of those files can be seen using the bash less command, which prints the contents of a file, as **Mr Neutron** does below,

.. code-block:: bash

    $ cd requirements
    $ less conda.txt
    numpy
    matplotlib-base
    $ less pip.txt
    numpy
    matplotlib

In general, ``conda.txt`` and ``pip.txt`` will contain the same list of dependencies. They are the dependencies that will be installed when installing from conda and PyPI, respectively. The reason we need separate files is that some packages have a different name on Conda and PyPI, respectively. For example, to install the lightest-weight vesrsion of ``matplotlib``, for historical reasons, the Conda package is called ``matplotlib-base`` while it is ``matplotlib`` on PyPI. Any other such differences in package names across conda-forge and PyPI can also be handled this way.

Second, **Mr Neutron** must build a virtual environment and install his new ``scikit-package`` package in it. **Mr Neutron** decides to create a new conda environment dedicated for his ``diffraction-utils`` package (he could have chosen to install the package in one of his existing environments). He first deactivates the ``skpkg-env`` (conda deactivate) as he has finished the work of using ``scikit-package`` to create a new project. He then creates a new conda environment called ``diff-utils-env`` using Python 3.14, installing the dependencies listed under ``conda.txt``, and builds and installs his own ``diffraction-utils`` package, using the following commands:

.. code-block:: bash

    $ cd ~/dev/diffraction-utils
    $ conda create -n diff-utils-env python=3.14
    $ conda activate diff-utils-env
    $ conda install --file requirements/conda.txt
    $ pip install . --no-deps

To test the installed package, **Mr Neutron** imports the ``DiffractionObject`` class from the ``diffraction-utils`` package in a Python module called ``neutron.py``, located in the folder path ``/data-analysis/neutron-experiment/``. **Mr Neutron** writes the following line at the top of the ``neutron.py`` file to import the ``DiffractionObject`` class,

.. code-block:: bash

    # ~/data-analysis/neutron-experiment/neutron.py
    from diffraction_utils.diffraction_objects import DiffractionObject

without having to change any of the other code. With the ``diff-utils-env`` environment activated, **Mr Neutron** can run the code below:

.. code-block:: bash

    # cd ~/data-analysis/neutron-experiment
    $ python neutron.py

We note that, since **Mr Neutron** is the developer and wants to update the code as he is working, he can installs the package in his environment in “editable” mode (recommended) where he replaces the command ``pip install .`` with the following:

.. code-block:: bash

    $ pip install -e .

As long as **Mr Neutron** has activated the ``diff-utils-env`` conda environment, whenever he runs code anywhere on his computer it will run the version of the code it finds on disc at run-time without him having to reinstall the package. This is very convenient for developers, but is not the preferred installation method for users.

Use Git to track changes
------------------------

As the next step, **Mr Neutron** wants to continuously maintain the ``diffraction-utils`` package. The best way to do this is to use Git. It is beyond the scope of this article to explain Git in detail, but the main concept is that Git maintains a database on the computer with every version of every file in the user's project, so the user never loses work and can find any earlier version. Every time **Mr Neutron** “commits” the edits to the Git database, it stores the edits.

To set up Git, **Mr Neutron** types the following command once to initiate the Git database for the project folder (including subdirectories):

.. code-block:: bash

    # ~/dev/diffraction-utils
    $ git init

**Mr Neutron** then creates the first commit through the following commands:

.. code-block:: bash

    $ git add .
    $ git commit -m "initial commit of the package files"

The ``git add .`` command adds all the files in the current directory (including subdirectories) to the list of files that will be committed to the database next time the user makes a commit. The ``git commit`` command actually commits those edits and changes to the database with a clear commit message describing the edits.

Set up pre-commit hooks to automatically check syntax
------------------------------------------------------

Once the local repository is under Git control, **Mr Neutron** wants to ensure that the code is properly formatted *before* committing to the Git database. This can be done by triggering ``pre-commit`` to run each time a new commit is attempted. This is done with a ``pre-commit`` hook. A hook automatically runs a program, or programs, before making a Git commit, every time **Mr Neutron** runs ``git commit``. ``scikit-package`` uses the ``pre-commit`` package to manage this. To get this set up, **Mr Neutron** (who has already installed the ``pre-commit`` package in his environment with ``conda install pre-commit``), types this command:

.. code-block:: bash

    $ precommit install

Now, every time **Mr Neutron** runs git commit -m "<commit message>", he will see in the terminal the hooks being executed, for example:

.. code-block:: bash

    $ git commit -m "chore: implement local precommit hooks"
    black...........................................................Passed
    prettier........................................................Passed
    docformatter....................................................Passed

**Mr Neutron** proceeds to add new features and bug-fixes to the diffraction-utils package and committing the changes, but sometimes ``pre-commit`` hooks fail. If this happens, **Mr Neutron** will see that the most recent commit was not written to the Git database, for example by using the ``git log`` command. **Mr Neutron** can then fix those errors manually and rerun ``git commit``.

At any time, **Mr Neutron** can use the ``pre-commit run --all-files`` command to trigger ``pre-commit`` manually while fixing those errors so that he does not have to make a commit to run the checks. As discussed in Section 2, ``pre-commit`` auto-fixes based on the configurations provided in ``.pre-commit-config.yaml`` in the project directory. The output from ``pre-commit`` informs **Mr Neutron** which files, and which line in the file, caused the error, helping him fix everything up.

Use GitHub to backup code online
---------------------------------

Having successfully made edits to the code and commit them to his local Git database, **Mr Neutron** now wants to back-up his work online. ``scikit-package`` is integrated with GitHub which is a cloud-based platform for uploading and sharing Git projects.

**Mr Neutron** first creates a new repository on GitHub in his user space, mrneutron(he could create it in any organization that he owns) and enters diffraction-utils for the repository name. He selects the option to create an empty repository (without an auto- generated ``README``, ``.gitignore``, or ``LICENSE`` file) since these files are already created with ``scikit-package``. **Mr Neutron** connects the local to the remote (cloud) repository by typing:

.. code-block:: bash

    # ~/dev/diffraction-utils
    $ git remote add origin https://github.com/mrneutron/diffraction-utils.git

The term origin is an alias (name) for the remote repository. **Mr Neutron** then uploads the local repository content to the remote repository with:

.. code-block:: bash

    $ git push --set-upstream origin main

**Mr Neutron** can view the content uploaded to the remote GitHub repository. He can also make edits directly on the remote repository and synchronize those changes with the local repository using the ``git pull origin main`` command.

Use GitHub to share code with colleagues
----------------------------------------

**Mr Neutron** now wants to share the code with colleagues. The simplest way to do this is by sharing the public URL of the GitHub repository, which colleagues can use to download the code either from the website directly or through cloning, like shown below:

.. code-block:: bash

    $ git clone https://github.com/mrneutron/diffraction-utils.git

If for some reason **Mr Neutron** created the repository as a private repository rather than a public one, **Mr Neutron** can still share it with trusted colleagues by adding their GitHub usernames in the :guilabel:`Settings` page of the GitHub repository. Or, in the spirit of open science, he can make the repository public.

As mentioned, ``scikit-package`` already created a simple ``README.md`` file, which by default is displayed at the repository landing page on GitHub. The ``README.md`` contains basic instructions for how the colleague can clone and install the package. **Mr Neutron** can edit the ``README.md`` file to make things even clearer.

This completes the ``scikit-package`` Level 4 example. In the following example, we show you how to create and maintain professional-grade software for public distribution. Git and GitHub offer much more than just backing up or sharing code, as described so far. In :ref:`example-2`, we explore more advanced features such as using branches, creating pull requests, and running automated workflows.
