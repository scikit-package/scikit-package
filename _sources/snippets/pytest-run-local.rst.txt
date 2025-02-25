.. _test-package-locally:

.. code-block:: bash

    # Create a new environment, specify the Python version and install packages
    conda create -n <package_name>_env python=3.13 \
        --file requirements/test.txt \
        --file requirements/conda.txt \
        --file requirements/build.txt

    # Activate the environment
    conda activate <package_name>_env

    # Install your package locally
    # `--no-deps` to NOT install packages again from `requirements.pip.txt`
    pip install -e . --no-deps

    # Run pytest locally
    pytest

    # ... run example tutorials
