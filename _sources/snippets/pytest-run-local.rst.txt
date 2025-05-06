.. _test-package-locally:

.. code-block:: bash

    # Create a new environment, without build dependencies (pure Python package)
    $ conda create -n <package_name>-env python=3.13 \
        --file requirements/test.txt \
        --file requirements/conda.txt

    # Create a new environment, with build dependencies (non-pure Python package)
    $ conda create -n <package_name>-env python=3.13 \
        --file requirements/test.txt \
        --file requirements/conda.txt \
        --file requirements/build.txt

    # Activate the environment
    $ conda activate <package_name>-env

    # Install your package locally
    # `--no-deps` to NOT install packages again from `requirements.pip.txt`
    $ pip install -e . --no-deps

    # Run pytest locally
    $ pytest

    # ... run example tutorials
