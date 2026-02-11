#. Create a new conda environment. Let's call this environment ``my-package-env``:

    .. code-block:: bash

        conda create -n my-package-env python=3.14 \
            --file requirements/conda.txt \
            --file requirements/tests.txt

#. Activate the conda environment:

    .. code-block:: bash

        conda activate my-package-env

#. Build and install the package locally:

    .. code-block:: bash

        pip install -e . --no-deps

    .. note:: What is the ``-e`` flag?

        The ``-e`` flag indicates that you want to install the package in "editable" mode, which means that any changes you make to the source code will be reflected immediately without needing to reinstall the package. This is useful for development purposes.

    .. note:: What is the ``--no-deps`` flag?

        The ``--no-deps`` flag tells pip not to install any dependencies listed in ``requirements/pip.txt``. This is because we have already installed the dependencies in the conda environment using the command above.

    .. seealso::

        Why is it required to list dependencies both under ``pip.txt`` and ``conda.txt``? Please refer to the FAQ section :ref:`faq-dependency-management`.

#. Then, run the tests using the following command:

    .. code-block:: bash

        pytest

#. Ensure tests all pass with green checkmarks. Notice that in ``tests/test_functions.py``, we are importing the locally installed package.

#. Done!
