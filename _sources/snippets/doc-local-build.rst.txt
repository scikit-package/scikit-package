#. Install documentation related dependencies:

    .. code-block:: bash

        conda install --file requirements/docs.txt

#. Enter into the ``docs`` project directory and render documentation:

    .. code-block:: bash

        cd docs
        make html

#. Open the rendered documentation via web browser:

    .. code-block:: bash

        open _build/html/index.html

#. Here is a shortcut if you want to use it from the root directory of the project:

    .. code-block:: bash

        cd docs && make html && open _build/html/index.html && cd ..

    .. seealso::

        You can use a ``alias`` shortcut. Open ``~/.bashrc`` in your text editor and add the following line:

        .. code-block:: bash

            alias doc='cd docs && make html && open _build/html/index.html && cd ..'

        Apply the changes to your current terminal session:

        .. code-block:: bash

            source ~/.bashrc

        Now, you can simply enter the ``docs`` command in your terminal to build and open the documentation:

        .. code-block:: bash

            doc

(Optional for macOS/Linux only) Do you want to re-render documentation without running ``doc`` command every time? You can use ``sphinx-reload``.

    #. Install the dependencies including ``sphinx-reload`` sourced from ``PyPI``:

        .. code-block:: bash

            conda install --file requirements/docs.txt
            pip install sphinx-reload

    #. Run the following command to start live-reloading:

        .. code-block:: bash

            sphinx-reload docs

    #. Now, each time you make changes to the documentation, it will be automatically reloaded in your web browser.
