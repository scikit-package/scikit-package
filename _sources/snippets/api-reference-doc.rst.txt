If you want to build the API documentation for your package, like https://www.diffpy.org/diffpy.utils/api/diffpy.utils.html, here is a quick guide for you.

First, check whether your package is a standard package or a package that supports namespace imports.

- If your package can be imported as ``import <package_name>``, you can use ``sphinx-apidoc`` to generate the API ``.rst`` files each time your documentation is re-rendered. Follow the instructions :ref:`here <faq-doc-api-standard>`.

- If your package supports **namespace import**, like ``import <namespace_name>.<package_name>``, you can use our script called ``auto_api.py`` to generate the API documentation. Follow the instructions :ref:`here <faq-doc-api-namespace>`.

.. note:: Do you want to know the difference in folder structure between a package that uses regular imports vs. namespace imports? Please check the FAQ section on :ref:`package structure <faq-project-setup-namespace>`.
