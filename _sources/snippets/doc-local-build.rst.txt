#. Install the requirements for building the documentation.

    .. code-block:: bash

        $ conda install --file requirements/docs.txt

#. Then we will use an external tool called ``sphinx-reload`` to automatically reload the documentation when you make changes to ``.rst`` files.

    .. code-block:: bash

        $ pip install sphinx-reload

    .. note::

        ``sphinx-reload`` is only available via pip install.

#. A HTML will appear automatically in your browser by running the following command:

    .. code-block:: bash

        $ sphinx-reload doc

.. note::

    If you see the error "No module named" (e.g., ``WARNING: autodoc: failed to import module 'tools' from module 'diffpy.pdfmorph'; the following exception was raised: No module named 'diffpy.utils'``), it can be resolved by adding ``autodoc_mock_imports = [<pkg>]`` to your ``conf.py`` right under imports. This file is located in ``/doc/source/conf.py``.
