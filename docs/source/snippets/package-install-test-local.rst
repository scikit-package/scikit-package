#. Create a new conda environment. Let's call this environment ``my-package-env``:

    .. code-block:: bash

        conda create -n my-package-env python=3.14 \
            pip setuptools setuptools-git-versioning \
            --file requirements/conda.txt \
            --file requirements/tests.txt

    .. note::

        Package names must be listed **before** the ``--file`` options, as shown above. ``conda`` does not accept them afterwards.

#. Activate the conda environment:

    .. code-block:: bash

        conda activate my-package-env

#. Build and install the package locally:

    .. code-block:: bash

        pip install -e . --no-deps --no-build-isolation

    The goal of these three flags together is that **every package in the environment comes from conda-forge, exactly as it will in production**, and ``pip`` does nothing except link your local source code into the environment. Nothing is downloaded from PyPI.

    .. note:: What is the ``-e`` flag?

        The ``-e`` flag indicates that you want to install the package in "editable" mode, which means that any changes you make to the source code will be reflected immediately without needing to reinstall the package. This is useful for development purposes.

    .. note:: What is the ``--no-deps`` flag?

        The ``--no-deps`` flag tells pip not to install any dependencies listed in ``requirements/pip.txt``. This is because we have already installed the dependencies in the conda environment using the command above.

    .. note:: What is the ``--no-build-isolation`` flag?

        To build your package, pip needs the build backend listed under ``[build-system]`` in ``pyproject.toml``, which for a ``scikit-package`` project is ``setuptools`` and ``setuptools-git-versioning``. By default pip ignores what is already installed and downloads its own copies **from PyPI** into a temporary environment. ``--no-deps`` does not prevent this, because the build backend is not a dependency of your package.

        The ``--no-build-isolation`` flag tells pip to use the build backend already installed in your conda environment instead, which is why ``setuptools`` and ``setuptools-git-versioning`` are added to the ``conda create`` command above.

    .. seealso::

        Why is it required to list dependencies both under ``pip.txt`` and ``conda.txt``? Please refer to the FAQ section :ref:`faq-dependency-management`.

#. Then, run the tests using the following command:

    .. code-block:: bash

        pytest

#. Ensure tests all pass with green checkmarks. Notice that in ``tests/test_functions.py``, we are importing the locally installed package.

#. Done!
