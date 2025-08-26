(Required) Use conda environment to install packages and run Python code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Virtual environments allow you to create isolated environments, each with their own software package versions installed. This is especially helpful when working with multiple different software programs that require conflicting versions of the same packages and is overall a good practice.

``conda`` is an open-source package and environment management software that allows you to create isolated environments to install software, including Python and its packages.

#. Install ``conda`` by following the installation guide of ``miniconda`` found at https://www.anaconda.com/docs/getting-started/miniconda/main.

#. Add the ``conda-forge`` channel to your conda configuration by running the following command:

    .. code-block:: bash

        conda config --add channels conda-forge

#. Now, let's create a new environment and install ``numpy`` in it. ``numpy`` will be sourced from the ``conda-forge`` channel. Replace ``<project-name>`` with the name of your project.

    .. code-block:: bash

        # Create a new environment and install numpy in the environment
        conda create -n <project-name>-env numpy

        # Activate the environment
        conda activate <project-name>-env

#. Let's check if the installation was successful. You can do this by running the following command:

    .. code-block:: bash

        python --version

    .. note::

        If you are a Windows PowerShell user and Python is not found after activating the environment, you can run the following command:

        .. code-block:: bash

            # For Windows (PowerShell)
            conda init powershell

#. Done!
