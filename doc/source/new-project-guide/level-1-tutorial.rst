Overview
^^^^^^^^

By the end of this tutorial, you will be able to reuse code within a file by creating a function. This is the first step in reusing code in Python. You will learn how to create a function and call it multiple times within the same file.

Prerequisites
^^^^^^^^^^^^^

We assume you have a basic understanding of how to execute a Python script in a command-line tool.

Also, ensure that Python is installed on your system. You can check this by running the following command:

.. code-block:: bash

    python --version

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

    pip install numpy

Then run

.. code-block:: bash

    python example_code.py

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

.. _conda-setup-simple:

.. include:: snippets/conda-env-setup-simple.rst

What's next?
^^^^^^^^^^^^

You may proceed to Level 2 below. You will learn to share the ``dot_product`` across multiple Python files and modules.
