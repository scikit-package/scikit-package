#######
|title|
#######

.. |title| replace:: scikit-package documentation

| Software version |release|.
| Last updated |today|.

Welcome to Billinge Group's Python scikit-package documentation!

Statement of need
-----------------

Your research impact can be amplified by distributing your contributions through well-documented software packages. However, creating these packages requires time dedicated to software infrastructure and ongoing maintenance. ``scikit-package`` is a Python package standard and generator that helps you launch new scientific code or migrate existing ones.

``scikit-package`` provides research-quality documents suitable for open-source development and supports Python versions compatible with the `SPEC0 <https://scientific-python.org/specs/spec-0000/>`_ proposal through automated workflows. Additionally, it offers a streamlined process for building and distributing your scientific software, ensuring reproducibility across all major operating systems. With ``scikit-package``, you can focus on developing your scientific code while ensuring it reaches a broader audience.

What are the useful features?
-----------------------------

To help increase your research impact, ``scikit-package`` offers the following features:

- Automated `PEP8 <https://peps.python.org/pep-0008/>`_ and `PEP256 <https://peps.python.org/pep-0256/>`_ standard checks.
- Automated PyPI/GitHub release, testing, documentation, and CHANGELOG updates.
- Streamlined package release workflow with a checklist.
- Latest Python version support compatible with `SPEC0 <https://scientific-python.org/specs/spec-0000/>`_.
- Rich README template containing badges, installation, support, and contribution guide.
- Automatic spelling check, linting for .json, .yml, and .md files.

For more technical details, it includes:

- Pull requests with coverage reports using ``Codecov`` and checks with ``pre-commit CI``.
- Namespace package support, e.g., ``import diffpy.utils``.
- conda-package ``meta.yaml`` generation with a template.
- Support for non-pure Python package releases with ``cibuildwheel``.
- Support for headless GitHub CI testing for GUI applications.
- Reusable GitHub Actions workflows located in `Billingegroup/release-scripts <https://github.com/Billingegroup/release-scripts/tree/main/.github/workflows>`_.

How do I get started?
---------------------

Please visit the :ref:`Getting started <getting-started>` page to learn how to navigate the documentation!

How do I receive support?
-------------------------

If you have any questions or have trouble, please read the :ref:`Frequently asked questions (FAQ) <frequently-asked-questions>` section to see if your questions have already been answered. If there aren't answers available, please create an issue. The team will reach out.

How can I contribute?
---------------------

Do you have any new features? Please make an issue via the GitHub issue tracker for further discussions. For a minor typo or grammatically incorrect sentence, please make a pull request. Before making a PR, please run ``pre-commit run --all-files`` to ensure the code is formatted.

Who are using ``scikit-package``?
----------------------------------

The full list of packages is as follows:

- `diffpy.pdffit2 <https://github.com/diffpy/diffpy.pdffit2>`_
- `diffpy.fourigui <https://github.com/diffpy/diffpy.fourigui>`_
- `diffpy.pdfgui <https://github.com/diffpy/diffpy.pdfgui>`_
- `diffpy.utils <https://github.com/diffpy/diffpy.utils>`_
- `diffpy.structure <https://github.com/diffpy/diffpy.structure>`_
- `diffpy.labpdfproc <https://github.com/diffpy/diffpy.labpdfproc>`_
- `diffpy.pdfmorph <https://github.com/diffpy/diffpy.pdfmorph>`_
- `diffpy.snmf <https://github.com/diffpy/diffpy.snmf>`_
- `diffpy.srmise <https://github.com/diffpy/diffpy.srmise>`_
- `regolith <https://github.com/regro/regolith>`_
- `bg-mpl-stylesheets <https://github.com/Billingegroup/bg-mpl-stylesheets>`_

=======
Authors
=======

- Sangjoon Lee (sl5400@columbia.edu)
- Andrew Yang (ay2546@columbia.edu)
- Simon Billinge (sb2896@columbia.edu)

scikit-package is developed by Billinge Group and its community contributors.

For a detailed list of contributors, see
https://github.com/Billingegroup/scikit-package/graphs/contributors.

================
Acknowledgements
================

The Billinge Group's scikit-package has been modified from the NSLS-II scientific cookiecutter: https://github.com/nsls-ii/scientific-python-cookiecutter

=================
Table of contents
=================
.. toctree::
   :maxdepth: 2

   getting-started
   skpackage-guide
   release-guide
   conda-forge-guide
   frequently-asked-questions
   license
   release

=======
Indices
=======

* :ref:`genindex`
* :ref:`search`
