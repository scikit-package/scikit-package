Follow these steps sequentially:

.. code-block:: bash

    # Create a new environment, specify the Python version and install packages
    conda create -n <project-name>_env \
        --file requirements/test.txt \
        --file requirements/conda.txt \
        --file requirements/build.txt

    # Activate the environment
    conda activate diffpy_utils_env

    cd doc
    make html
    open open build/html/index.html

To run as a single command:

.. code-block:: bash

    cd doc && make html && open build/html/index.html && cd ..

Your default browser will open the documentation in a new window.
