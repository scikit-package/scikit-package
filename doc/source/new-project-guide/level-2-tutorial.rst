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

Make sure you follow the instructions provided above in Level 1 :ref:`here<setup-up-conda-environment-with-numpy>`

What's next?
^^^^^^^^^^^^

In Level 3, you will learn to reuse code across multiple files and folders. You will also learn to run tests and format your code automatically using ``pre-commit``.
