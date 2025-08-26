Install ``scikit-package`` with conda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Ensure that ``conda`` is installed on your local computer as instructed in :ref:`conda-env-setup-simple`.

#. Ensure that you have added the ``conda-forge`` channel to your ``conda`` configuration.

    .. code-block:: bash

        conda config --add channels conda-forge

#. Create a new conda environment ``skpkg-env`` and install ``scikit-package`` and ``pre-commit`` simultaneously by running the following command:

    .. code-block:: bash

        conda create -n skpkg-env scikit-package pre-commit

    .. note::

        If the above command does not work, ensure you have added the ``conda-forge`` channel to your ``conda`` configuration in Step 2.
#. Activate the environment:

    .. code-block:: bash

        conda activate skpkg-env

#. Confirm that you have the latest version of ``scikit-package`` available on GitHub:

    .. code-block:: bash

        pip show scikit-package
