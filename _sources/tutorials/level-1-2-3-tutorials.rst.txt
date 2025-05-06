.. _level-1-2-3-tutorials:

(Level 1-3) Reuse code within a file, across files and folders
==============================================================

.. _tutorial-level-1:

Level 1. Reuse code within a file
---------------------------------

Overview
^^^^^^^^

By the end of this tutorial, you will be able to reuse code within a file by creating a function. This is the first step in reusing code in Python. You will learn how to create a function and call it multiple times within the same file.

Prerequisites
^^^^^^^^^^^^^

We assume you have a basic understanding of how to execute a Python script in a command-line tool.

Also, ensure that Python is installed on your system. You can check this by running the following command:

.. code-block:: bash

     $ python --version

Folder structure
^^^^^^^^^^^^^^^^

Here is the folder structure for this example:

.. code-block:: text

    my_project/
    └── example_code.py

Example code
^^^^^^^^^^^^

In the ``example_code.py`` file, define a function called ``dot_product`` that takes two vectors as input and returns their dot product:

.. code-block:: python

    # example_code.py
    import numpy as np

    def dot_product(a, b):
        """Calculate the dot product of two vectors."""
        return np.dot(a, b)

In the same file, copy and paste the block of code below to reuse the function ``dot_product``.

.. code-block:: python

    # Reusing the function within the same file
    v1 = [1, 2]
    v2 = [3, 4]
    print(dot_product(v1, v2))  # returns 11

    v3 = [5, 6]
    v4 = [7, 8]
    print(dot_product(v3, v4))  # returns 83

Install ``numpy`` by running:

.. code-block:: bash

     $ pip install numpy

Then run

.. code-block:: bash

    $ python example_code.py

You should see the outputs of 11 and 83 printed.

Here is the full content of the ``example_code.py`` file:

.. code-block:: python

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

Congratulation! You are now able to reuse code within a file by creating a function. Before we move on to the next level, let's learn about setting up a ``conda`` environment to install packages and run Python code in the following section.

.. _conda-env-setup-simple:

.. include:: ../snippets/conda-env-setup-simple.rst

What's next?
^^^^^^^^^^^^

You may proceed to Level 2 below. You will learn to share the ``dot_product`` across multiple Python files and modules.

.. _tutorial-level-2:

Level 2. Reuse code across files
--------------------------------

Overview
^^^^^^^^^

In Level 1, you learned to use a block of code in a single file. In Level 2, you will learn to reuse the same code across multiple files. Hence, the name for this level of called ``module``. Again, you don't need to install ``scikit-package`` due to its simplicity.

Prerequisites
^^^^^^^^^^^^^^

If you are new to Python, make sure you have followed the instructions provided above in Level 1.

.. _level-2-folder-structure:

Folder structure
^^^^^^^^^^^^^^^^

Here is the project structure for this example:

.. code-block:: text

    my_project/
    ├── shared_functions.py
    ├── file_one.py
    └── file_two.py


Example code
^^^^^^^^^^^^^^

In ``shared_functions.py``, define a function called ``dot_product`` that takes two vectors as input and returns their dot product:

.. code-block:: python

    # shared_functions.py
    import numpy as np

    def dot_product(a, b):
        """Calculate the dot product of two vectors."""
        return np.dot(a, b)

For ``file_one.py`` and ``file_two.py``, you are able to import the function ``dot_product`` from the ``shared_functions.py`` file and use it in the same way as in Level 1.

This is the content of ``file_one.py``:

.. code-block:: python

    # file_one.py
    from shared_functions import dot_product

    v1 = [1, 2]
    v2 = [3, 4]
    print(dot_product(v1, v2))  # returns 11

This is the content of ``file_two.py``:

.. code-block:: python

    # file_two.py
    import shared_functions

    v3 = [5, 6]
    v4 = [7, 8]
    print(shared_functions.dot_product(v3, v4))  # returns 83

.. note::

    Notice that in ``file_two.py``, you can import the entire module ``shared_functions`` and use the function ``dot_product`` by prefixing it with the module name. Importing a modele is a good practice when you have multiple functions in the same file. This way, you can avoid name conflicts and make your code more readable.

Are you having trouble running the code?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make sure you follow the instructions provided above in Level 1 :ref:`here<conda-env-setup-simple>`

What's next?
^^^^^^^^^^^^

In Level 3, you will learn to reuse code across multiple files and folders. You will also learn to run tests and format your code automatically using ``pre-commit``.

Level 3. Reuse code across projects
-----------------------------------

Overview
^^^^^^^^^

The goal in Level 3 is to reuse code across multiple projects. Hence, the name associated with this level is ``workspace``. Each project could have many files that would utilize the reusable code.

Also, you will learn to execute and write **unit tests** for your reusable code. Unit tests are small, isolated tests that verify functionality. They help ensure that your code behaves as expected and can catch bugs early in the development process. You might want to run them before sharing code with others or deploying it to more projects.

Lastly, you will also learn to **automate formatting** to keep your code clean and consistent so that others, including you, can save time reading and adding new code.

This tutorial will take about 3-10 minutes.

.. include:: ../snippets/scikit-installation.rst

Initiate a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new project by running the following command:

.. code-block:: bash

     $ package create workspace

You will then be asked to enter the ``project-name``. The default value is ``workspace-folder``.
In this example, enter ``data-analysis-project`` as the workspace folder you are about to create.

.. code-block:: bash

     [1/1] workspace_name (workspace-folder): data-analysis-projects

``cd`` into the new directory created by the ``package create workspace`` command above:

.. code-block:: bash

    $ cd data-analysis-project

Folder structure
^^^^^^^^^^^^^^^^^

When you ``cd`` into the new directory, you will see a folder structure as shown below:

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

If you would like to add more projects, you can create a new folder under the root directory. For example, you can create a folder called ``proj-two`` and add your code there. This can be extrapolated for as many projects as you like:

.. code-block:: bash

     $ mkdir proj-two
     $ cd proj-two
     $ touch __init__.py
     $ touch proj_two_code.py


File descriptions
^^^^^^^^^^^^^^^^^^

Now that the folder structure is created, let's go through the files and folders in the project.

**Note:** The Python files (``.py``) and project structure shown here are example templates. You can **change file names, add files, edit contents, or replace the examples entirely** when creating your own project. These examples are intended to demonstrate key ideas like code reuse and organization.

- ``README.md`` is a markdown file for project documentation. Typically, it includes a project description, installation instructions, and usage examples. You can edit this file to add your own project information.

- ``shared_functions.py`` is the file where you define code you want to reuse. You can name this file whatever you like, and you can include multiple files here with different names for organizing reusable code. In the ``scikit-package`` template, we populate this file with the following example function to help demonstrate the concept of shared functions:

.. code-block:: python

     # shared_functions.py
     import numpy as np


     def dot_product(a, b):
          """Calculate the dot product of two vectors."""
          return np.dot(a, b)

- ``proj_one/proj_one_code.py`` shows an example of how to import and use the ``dot_product()`` function from ``shared_functions.py``:

.. code-block:: python

     # proj_one_code.py
     import shared_functions

     a = [1, 2, 3]
     b = [1, 2, 3]
     result = shared_functions.dot_product(a, b)
     print(result)

- ``__init__.py`` files mark directories as Python modules. These are empty by default at this level.

- ``requirements.txt`` lists your project's dependencies. These are Python packages that are used throughout your project(s), which in this case includes ``numpy`` and ``pytest``. Please refer to the section "**Install dependencies**" below for more details on how to install them. You can add any other dependencies you need in this file:

.. code-block:: python

     # requirements.txt
     numpy
     pytest

- The ``tests`` folder contains tests for your shared functions. For example, ``test_shared_functions.py`` includes tests for the ``dot_product()`` function using ``pytest``. General naming convention for test files is ``test_<module_name>.py``. Similarly, test function names should be ``test_<function_name>()``. This is how ``pytest`` recognizes them as test functions. This can also contain tests for your sub-project modules.

To write your own test, follow these steps:

1. Create your function in a module. For example, under the ``proj_one`` directory, you might create a module called ``my_module.py`` that defines a function ``my_function()``.

2. Create a corresponding test file in the ``tests`` directory. The test file should be named ``test_<module_name>.py`` — in this case, ``test_my_module.py``.

3. Inside the test file, create a function that tests your code. The test function should be named ``test_<function_name>()`` — in this case, ``test_my_function()``.

Following this naming pattern ensures that ``pytest`` can automatically discover and run your tests:

.. code-block:: python

     # test_shared_functions.py
     import numpy as np
     import pytest
     import shared_functions


     def test_dot_product_2D_list():
     a = [1, 2]
     b = [3, 4]
     expected = 11.0
     actual = shared_functions.dot_product(a, b)
     assert actual == expected


     def test_dot_product_3D_list():
     a = [1, 2, 3]
     b = [4, 5, 6]
     expected = 32.0
     actual = shared_functions.dot_product(a, b)
     assert actual == expected


     @pytest.mark.parametrize(
     "a, b, expected",
     [
          # Test whether the dot product function works with 2D and 3D vectors
          # C1: lists, expect correct float output
          ([1, 2], [3, 4], 11.0),
          ([1, 2, 3], [4, 5, 6], 32.0),
          # C2: tuples, expect correct float output
          ((1, 2), (3, 4), 11.0),
          ((1, 2, 3), (4, 5, 6), 32.0),
          # C3: numpy arrays, expect correct float output
          (np.array([1, 2]), np.array([3, 4]), 11.0),
          (np.array([1, 2, 3]), np.array([4, 5, 6]), 32.0),
     ],
     )
     def test_dot_product(a, b, expected):
     actual = shared_functions.dot_product(a, b)
     assert actual == expected

- ``.pre-commit-config.yaml`` is a configuration file for pre-commit hooks. To use ``pre-commit`` you must install the package with ``conda install pre-commit``. This file and its usage is described in more detail in the section "**Automatic code formatting with pre-commit**" below.


Install dependencies
^^^^^^^^^^^^^^^^^^^^

You can install the dependencies like ``numpy`` listed in ``requirements.txt`` by running the following command:

.. code-block:: bash

    $ pip install -r requirements.txt

Set PYTHONPATH
^^^^^^^^^^^^^^^

When code is shared across nested folders, you need to set the ``PYTHONPATH`` environment variable to the current working directory.

Type ``pwd`` in your command-line tool to see the current working directory.

.. code-block:: bash

     $ pwd

For a macOS user, it will print something like ``/Users/macbook/downloads/dev/scikit-package/workspace_folder``.

Copy and paste the value while replacing ``<path-to-your-workspace-folder>`` with the path printed above:

.. code-block:: bash

     # For macOS/Linux user
    $ export PYTHONPATH="${PYTHONPATH}:<path-to-your-workspace-folder>"

     # For Windows (Powershell) user
    $env:PYTHONPATH = "$env:PYTHONPATH;<path-to-your-workspace-folder>"

To avoid retyping this command every time you open a new terminal, you can add it to your shell configuration file. The configuration files most commonly used are ``.bashrc`` or ``.zshrc`` for macOS/Linux users, and ``$PROFILE`` for Windows users. These files are located at the root directory (``~``). To edit these files, run the command:

.. code-block:: bash

     # For macOS/Linux:
     # bash shell
     $ nano ~/.bashrc
     # zsh shell
     $ nano ~/.zshrc

     # For Windows PowerShell:
     $ notepad $PROFILE

Then, add the command to set ``PYTHONPATH`` at the end of the file:

.. code-block:: bash

     # For macOS/Linux (bash or zsh shell)
     $ echo 'export PYTHONPATH="${PYTHONPATH}:/path/to/your/workspace_folder"'

     # For Windows (PowerShell)
     $ echo '$env:PYTHONPATH = "$env:PYTHONPATH;/path/to/your/workspace_folder"'

After adding the command, restart your terminal or run the corresponding file to activate the changes through the commands below:

.. code-block:: bash

     # For macOS/Linux:
     # bash shell
     $ source ~/.bash_profile
     # zsh shell
     $ source ~/.zshrc

     # For Windows PowerShell:
     $ . $PROFILE

.. note::

   If you are using a Level 4 package layout, this step is not required because proper packaging eliminates the need to set ``PYTHONPATH`` manually.

Run your code
^^^^^^^^^^^^^

Then, you can run the code by running:

.. code-block:: bash

    python proj_one/reuse_code.py

Run tests
^^^^^^^^^^

To run tests using ``pytest``, ``cd`` to the top level directory and run the following command:

.. code-block:: bash

     pytest

This will run all tests located in the ``tests`` directory.

In general, it is bad practice to tolerate failing tests. Ignoring tests can lead to bad habits and you may miss important bugs in your code!

.. note ::

     ``pytest`` is a testing framework for Python. It will automatically discover and run all the test files in the ``tests`` folder.

.. _pre-commit-manual:

Automatic code formatting with ``pre-commit``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Notice that there is a hidden file called ``.pre-commit-config.yaml`` in the root directory. This file is used to configure pre-commit "hooks". These hooks are checks that can be automatically executed when you commit your code to Git, which you will do in Level 4.

In Level 3, you will run these hooks manually for simplicity.

Recall ``pre-commit`` has already been installed in the environment in the previous stage. Since ``pre-commit`` is meant to work with ``Git``, create a local Git folder in your project folder by running:

.. code-block:: bash

     git init
     git add .

.. note::

     If you don't understand Git/GitHub, don't worry. For Level 3, it's not needed, although it will be used in Level 4 where you will host your code on GitHub and use GitHub to run these ``pre-commit`` hooks automatically.

Format your code by running:

.. code-block:: bash

     pre-commit run --all-files

It will then show the following:

.. code-block:: text

     black....................................................................Passed
     prettier.................................................................Passed
     docformatter.............................................................Passed

.. note::

    ``black`` is a tool that automatically formats Python code to conform to the PEP 8 style guide. ``prettier`` is a tool that formats code in various languages, including ``.md``, ``.rst``, and ``.json`` files. ``docformatter`` is a tool that formats docstrings in Python code.

Run ``pre-commit run --all-files`` frequently while developing code.

What's next?
^^^^^^^^^^^^

Notice that it's quite annoying to set ``PYTHONPATH`` every time you open a new terminal. In Level 4, you will learn how to set it permanently by turning your software into a locally installed package. You will also learn to use ``Git`` and ``GitHub`` to host your code online and share it with others and also enjoy the benefits of ``pre-commit`` hooks and other automatic ``tests`` done not locally but also on GitHub's remote server known as "GitHub Actions".

We highly recommend you become familiar with Git/GitHub before proceeding to Level 4. Feel free to check out our GitHub workflow guide in the FAQ :ref:`here<faq-github-workflow>`.
