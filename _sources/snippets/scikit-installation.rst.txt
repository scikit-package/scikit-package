.. _scikit-package-installation:

Install ``scikit-package`` with conda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Ensure you have ``conda`` installed and the ``conda-forge`` channel added to your conda configuration. If you haven't, check :ref:`here<conda-env-setup-simple>` for instructions on how to install and include the ``conda-forge`` channel.

#. Create a new environment named ``<project>-env``, e.g., ``skpkg-env``. Install ``scikit-package`` and ``pre-commit`` simultaneously by running the following command:

    .. code-block:: bash

        $ conda create -n skpkg-env scikit-package pre-commit

#. Activate the environment:

    .. code-block:: bash

        $ conda activate skpkg-env

#. Confirm that you have the latest version of ``scikit-package`` available on GitHub:

    .. code-block:: bash

        $ pip show scikit-package
