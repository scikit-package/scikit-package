.. _level-1-2-3-tutorials:

(Level 1-3) Reuse code within a file, across files and folders
==============================================================

.. _tutorial-level-1:

Level 1. Reuse code within a file
---------------------------------

Overview
^^^^^^^^

By the end of this tutorial, you will be able to reuse code within a file by creating a function.

You will also learn the recommended way to use the Terminal to set up your computer and your Python
environment for development and distribution.

.. _conda-env-setup-simple:

.. include:: ../snippets/conda-env-setup-simple.rst

(Recommended) Setup for Windows users for command-line tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Are you a Windows user? Our preferred command-line application is **Git for Windows**. It supports Linux commands like ``mkdir`` and ``cd`` so that we all can follow the same commands in this tutorial and avoid confusion. You can download it from https://git-scm.com/download/win.

.. note::

     If you are a macOS or Linux user, you can use the built-in terminal.

Example
^^^^^^^

#. We will create a folder structure for this example:

     .. code-block:: text

          skpkg-tutorials/
          └── shared_functions.py

#. Open your command-line tool and type the following commands:

     .. code-block:: bash

          # Create a new directory
          mkdir skpkg-tutorials
          # Navigate into the directory
          cd skpkg-tutorials
          # Create a new file
          touch shared_functions.py

#. Copy and paste the code block below into ``shared_functions.py``:

     .. code-block:: python

          # shared_functions.py
          import numpy as np

          def dot_product(a, b):
               """Calculate the dot product of two vectors."""
               return np.dot(a, b)

          # Reusing the function within the same file
          v1 = [1, 2]
          v2 = [3, 4]
          print(dot_product(v1, v2))  # returns 11

          v3 = [5, 6]
          v4 = [7, 8]
          print(dot_product(v3, v4))  # returns 83

#. Run the code after activating your conda environment that you have created in :ref:`conda-env-setup-simple` above:

     .. code-block:: bash

          conda activate <env-name>
          python shared_functions.py

#. You should see the outputs of 11 and 83 printed.

What's next?
^^^^^^^^^^^^

Let's share the ``dot_product`` function across multiple Python files.

.. _tutorial-level-2:

Level 2. Reuse code across files
--------------------------------

Overview
^^^^^^^^^

In Level 2, you will reuse the same code across multiple files. Hence, the name for this level of called ``module``.

.. _level-2-folder-structure:


Example code
^^^^^^^^^^^^

#. Here is the following folder structure that we will create:

     .. code-block:: text

          skpkg-tutorials/
          ├── shared_functions.py
          ├── file_one.py
          └── file_two.py

#. Create ``file_one.py`` and ``file_two.py`` in the same directory as ``shared_functions.py`` that we created in Level 1:

     .. code-block:: bash

          cd skpkg-tutorials
          touch file_one.py file_two.py

#. Copy and paste the following to ``file_one.py``:

     .. code-block:: python

          # file_one.py
          from shared_functions import dot_product

          v1 = [1, 2]
          v2 = [3, 4]
          v1dotv2 = dot_product(v1, v2)
          print(v1dotv2)  # returns 11

     .. seealso::

          Use any IDE (Visual Studio Code, PyCharm, etc.) to create the files and copy-paste the code.

#. Copy and paste the following to ``file_two.py``:

     .. code-block:: python

          # file_two.py
          import shared_functions

          v3 = [5, 6]
          v4 = [7, 8]
          v3dotv4 = shared_functions.dot_product(v3, v4)
          print(v3dotv4)  # returns 83

     .. note::

          Notice that in ``file_two.py``, we imported the entire module ``shared_functions``.  When we did this, all the functions are imported but to access them you have to prefix the module name.
          This way, you can avoid name conflicts as well as making your code more readable.

#. As we have done in Level 1, activate the conda environment and run the code:

     .. code-block:: bash

          conda activate <env-name>
          python file_one.py
          python file_two.py

What's next?
^^^^^^^^^^^^

In Level 3, you will learn to reuse code across multiple files and folders. You will also learn to run tests and format your code automatically using ``pre-commit``.

Level 3. Reuse code across projects
-----------------------------------

Overview
^^^^^^^^^

The goal in Level 3 is to reuse code across multiple projects. Hence, the name associated with this level is ``workspace``. Each project could have many files that would utilize the reusable code.

Also, you will learn to execute and write **unit tests** for your reusable code. Unit tests are small, isolated tests that verify functionality. They help ensure that your code behaves as expected and can catch bugs early in the development process. You might want to run them before sharing code with others or deploying it to more projects.

Lastly, you will also learn to **automate formatting** to keep your code clean and consistent so that others, including future-you, can save time reading and adding new code.

This tutorial will take about 3-10 minutes.

Initiate a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Activate your conda environment you've created in :ref:`conda-env-setup-simple` above and install ``scikit-package``:

     .. code-block:: bash

          conda activate <env-name>
          conda install scikit-package

#. Create a new project by running the following command:

     .. code-block:: bash

          package create workspace

     .. note::

          Did you encounter an error with the above command? You may need to install Git on your computer. For Windows, we recommend installing Git for Windows (https://gitforwindows.org/) and for macOS/Linux, install Git from https://git-scm.com/downloads. Once Git is installed, try the command again after restarting your terminal.

#. Enter ``data-analysis-project`` for the ``project-name``:

     .. code-block:: bash

          [1/1] workspace_name (workspace-folder): data-analysis-projects

#. ``cd`` into the new directory:

     .. code-block:: bash

          cd data-analysis-project

#. Confirm you have the following folder structure generated:

     .. code-block:: text

          data-analysis-project/
          ├── README.md
          ├── requirements.txt
          ├── shared_functions.py
          ├── proj-one
          │   ├── __init__.py
          │   └── proj_one_code.py
          └── tests
               ├── __init__.py
               └── test_shared_functions.py


File descriptions
^^^^^^^^^^^^^^^^^^

Let's go through some important files and their purposes:

.. note::

     - ``README.md`` is a markdown file for project documentation. Typically, it includes a project description, installation instructions, and usage examples. You can edit this file to add your own project information.

     - The ``__init__.py`` file, when placed inside a directory, tells Python to treat that directory as a package, which can contain modules. A Python module is a file with a ``.py`` extension that contains Python code. The ``__init__.py`` file is empty in the ``workspace`` level.

     - The ``tests`` folder contains tests for your shared functions. For example, ``test_shared_functions.py`` includes tests for the ``dot_product()`` function using ``pytest``. General naming convention for test files is ``test_<module_name>.py``. Similarly, test function names should be ``test_<function_name>()``. This is how ``pytest`` recognizes them as test functions. This can also contain tests for your sub-project modules.

Run code after setting PYTHONPATH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before running code, you need to set the ``PYTHONPATH`` environment variable to the current working directory.

#. Type ``pwd`` in your command-line tool to see the present working directory.

     .. code-block:: bash

          pwd

     For a macOS user, it will print something like ``/Users/imac/dev/data-analysis-projects``.

#. Replace ``<path-to-your-workspace-folder>`` with the output of ``pwd`` in the command below:

     .. code-block:: bash

          # For macOS/Linux/Git for Windows user
          export PYTHONPATH="${PYTHONPATH}:<path-to-your-workspace-folder>"

          # For Windows (Powershell) user
          env:PYTHONPATH = "$env:PYTHONPATH;<path-to-your-workspace-folder>"

#. Install the dependencies:

     .. code-block:: bash

          conda activate <env-name>
          conda install --file requirements.txt

     .. note::

          The ``requirements.txt`` file contains the list of dependencies required for your project. In this case, it includes ``numpy`` and ``pytest``. You can add more for your project as needed.

#. Run the code in ``proj_one/proj_one_code.py``:

     .. code-block:: bash

          cd proj-one
          python proj_one_code.py

#. Also run the tests:

     .. code-block:: bash

          cd ..        # go back to the parent directory to run pytest
          pytest

     You should see the output similar to:

     .. code-block:: text

          ========================== test session starts ==========================
          platform darwin -- Python 3.xx
          rootdir: /Users/imac/dev/
          configfile: pyproject.toml
          plugins: env-1.1.5, cov-6.1.1
          collected 8 items

          tests/test_shared_functions.py ........                           [100%]

          =========================== 8 passed in 0.30s ===========================

     .. note::

          In general, it is bad practice to tolerate failing tests. Ignoring tests can lead to bad habits and you may miss important bugs in your code!

.. _pre-commit-manual:

Automatic code formatting with ``pre-commit``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to automatically format code syntax to make it more standard and
more readable. ``pre-commit`` is a tool that helps you with that.

#. Install ``pre-commit`` by running the following command:

     .. code-block:: bash

          conda activate <env-name>
          conda install pre-commit

     .. note::

          ``pre-commit`` is a framework for managing and maintaining multi-language pre-commit hooks. It allows you to automatically format your code before committing it to a version control system like Git.

#. Initiate ``Git`` and stage all files generated by the ``package create workspace`` command to the local Git database:

     .. code-block:: bash

          git init
          git add .

     .. note::

          If you don't understand Git/GitHub, don't worry. For Level 3, it's not needed, although it will be used in Level 4 where you will host your code on GitHub and use GitHub to run these ``pre-commit`` hooks automatically.

#. Format your code by running:

     .. code-block:: bash

          pre-commit run --all-files

#. It will then show the following:

     .. code-block:: text

          black....................................................................Passed
          prettier.................................................................Passed
          docformatter.............................................................Passed

     .. note::

          ``black`` is a tool that automatically formats Python code to conform to the PEP 8 style guide. ``prettier`` is a tool that formats code in various languages, including ``.md``, ``.rst``, and ``.json`` files. ``docformatter`` is a tool that formats docstrings in Python code.

#. Done! Run ``pre-commit run --all-files`` frequently while developing code to keep your code in good shape.

What's next?
^^^^^^^^^^^^

Congratulations! You have completed Level 3. In Level 4, you will learn to host your code on GitHub and automate code linting and testing using GitHub Actions.

Before that, we highly recommend you become familiar with Git/GitHub before proceeding to Level 4 with basic concepts provided in :ref:`faq-github-workflow`.

When you are ready, you can proceed to the next tutorial: :ref:`level-4-tutorial`.

(Optional) How to set PYTHONPATH permanently
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To avoid retyping this command every time you open a new terminal, you can add it to your shell configuration file. The configuration files most commonly used are ``.bashrc`` or ``.zshrc`` for macOS/Linux/Git for Windows users, and ``$PROFILE`` for Windows users. These files are located at the root directory (``~``).

#. To edit these files, run the command:

     .. code-block:: bash

          # For macOS/Linux/Git for Windows:
          # bash shell
          nano ~/.bashrc
          # For Windows PowerShell:
          notepad $PROFILE

#. Add the command to set ``PYTHONPATH`` at the end of the file:

     .. code-block:: bash

          # For macOS/Linux/Git for Windows
          echo 'export PYTHONPATH="${PYTHONPATH}:/path/to/your/workspace_folder"'

          # For Windows (PowerShell)
          echo '$env:PYTHONPATH = "$env:PYTHONPATH;/path/to/your/workspace_folder"'

#. Save the file.

#. Run the following command to apply the changes:

     .. code-block:: bash

          # For macOS/Linux/Git for Windows:
          source ~/.bashrc
          # For Windows PowerShell:
          . $PROFILE

#. Restart your terminal.

#. Done! Now you can run your Python code without setting ``PYTHONPATH`` every time.

(Optional) How to create a new project folder?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is an example of how to create an additional project under the same workspace folder you created in Level 3. We will create a new project named ``proj-two``.

#. Move into the workspace folder:

     .. code-block:: bash

          cd data-analysis-project

#. Create a new directory and two files in it:

     .. code-block:: bash

          mkdir proj-two
          cd proj-two
          touch __init__.py proj_two_code.py

#. Add your code to ``proj_two_code.py``.

#. Run the code:

     .. code-block:: bash

          cd proj-two
          python proj_two_code.py

#. Done! You can also start writing tests for this new project in the ``tests`` folder by creating a new file named ``test_proj_two_code.py``.
