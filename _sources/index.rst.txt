| Software version |release|
| Last updated |today|.

Welcome to the ``scikit-package`` official documentation!

``scikit-package`` offers tools and practices for the scientific community to make better and more reusable Scientific Python packages and applications.

How to cite ``scikit-package``
------------------------------

If you use ``scikit-package`` to standardize your Python software, we would like you to cite scikit-package:

  S. Lee and C. Myers and A. Yang and T. Zhang and S. J. L. Billinge, scikit-package - software packaging standards and roadmap for sharing reproducible scientific software (https://arxiv.org/abs/2507.03328)

How does ``scikit-package`` benefit scientists?
-----------------------------------------------

``scikit-package`` offers step-by-step instructions for reusing and sharing code, starting from something as simple as defining and using functions, all the way to maintaining and releasing a fully documented open-source package on PyPI and conda-forge.

Here are the 3 goals of ``scikit-package`` for the scientific community:

#. We help scientists share scientific code to **amplify research impact**.

#. We help scientists save time, allowing them to **focus on writing scientific code**.

#. We offer **best practices** from the Billinge group's experience in developing scientific software.

Here is an overview of the five levels of reusing and sharing code and the key features of ``scikit-package``:

.. image:: ../../img/figures/scikit-package-overview-qr-code.png
    :alt: Diagram of 5 levels of sharing code with key features and scikit-package commands
    :width: 800px
    :align: center

The steps are divided into five levels of shareability and complexity, allowing users to choose the level that best suits their current needs. Code can be moved to higher levels as necessary.

- Level 1, ``function``, which is already widely used, consists of simply defining functions within the same file or module.

- Level 2, ``module``, expands on Level 1 by reusing functions across separate module files within the same directory.

- Level 3, ``workspace``, restructures the organization so that a block of code can be reused across multiple projects.

- Level 4, ``system``, enables users to create a lightweight package so that the code can be reused across all files locally.

- Level 5, ``public``, is the final step, where the source code is uploaded online so that anyone in the world can install the package, sourced from PyPI or conda-forge.

Who is using ``scikit-package``?
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
- `cifkit <https://github.com/bobleesj/cifkit>`_
- `SAF <https://github.com/bobleesj/structure-analyzer-featurizer>`_
- `CAF <https://github.com/bobleesj/composition-analyzer-featurizer>`_
- `bobleesej.utils <https://github.com/bobleesj/bobleesj.utils>`_
- ...

How do I get started?
---------------------

Please visit the :ref:`Overview <overview>` page to learn how to navigate the documentation!

Demo
----

Here is how you can use the ``package create public`` command to create a new Level 5 Python package called ``diffpy.my-project`` in just 1–2 minutes:

.. image:: ../../img/gif/demo.gif
   :alt: Demo of generating a new Level 5 package using scikit-package
   :align: center

Of course, you can start a lightweight package (Level 4) using the ``package create system`` command.

What are the full benefits when I reach Level 5?
-------------------------------------------------

- **Streamline the release process** by pushing a Git tag to trigger a sequence of actions: publishing to PyPI and GitHub, updating hosted documentation, and updating the ``CHANGELOG.rst`` file. Visit :ref:`release-pypi-github` for more details.
- **Host documentation with a public URL** using a ``Sphinx`` template as part of the PyPI and GitHub release. Includes live rendering, API documentation, and previews for each pull request.
- **Set custom default metadata** such as authors, project description, license holders, and keywords when creating a new package. Automatically store and reuse the entered metadata to update your package with the latest version of the ``scikit-package`` standards. To learn more, read :ref:`faq-set-default-prompt-value`.
- **Support namespace package imports** (e.g., ``import <org-name>.<package-name>``) to maintain branding consistency and avoid name collisions. To learn more, read :ref:`faq-project-setup-namespace`.

We have also adopted community software and standards in ``scikit-package``:

- Set up both local and remote ``pre-commit`` hooks to automate linting of code. This includes checks for `PEP8 <https://peps.python.org/pep-0008/>`_, `PEP 256 <https://peps.python.org/pep-0256/>`_, and static files such as ``.json``, ``.yml``, and ``.md``. Spelling checks are included as well. To learn more about the hooks provided at each level, read :ref:`faq-pre-commit-levels`.
- Provide a rich ``README.rst`` template that includes badges, installation instructions, support contacts, and contribution guidelines for your GitHub repository.
- Run ``pytest`` with the latest Python versions, adhering to the `SPEC0 <https://scientific-python.org/specs/spec-0000/>`_ specification, without requiring manual configuration.

For technical users, here are some of the advanced features:

- Streamline conda package release by updating ``meta.yaml`` with ``package create conda-forge`` after the PyPI and GitHub release. To learn more, read :ref:`release-conda-forge`.
- Support headless GitHub CI testing for GUI applications.
- Support non-pure Python package releases with ``cibuildwheel``.
- Reusable GitHub Actions workflows located in `scikit-package/release-scripts <https://github.com/scikit-package/release-scripts/tree/main/.github/workflows>`_.

How do I receive support?
-------------------------

If you have any questions or have trouble, please read the :ref:`Frequently asked questions (FAQ) <frequently-asked-questions>` section to see if your questions have already been answered. If there aren't answers available, please create `GitHub Issues <https://github.com/scikit-package/scikit-package/issues>`_.

How can I contribute to ``scikit-package``?
-------------------------------------------

Do you have any new features? Please make an issue via the GitHub issue tracker for further discussions. For a minor typo or grammatically incorrect sentence, please make a pull request. Before making a PR, please run ``pre-commit run --all-files`` to ensure the code is formatted.

=======
Authors
=======

- Sangjoon Lee (sl5400@columbia.edu)
- Caden Myers (cjm2304@columbia.edu)
- Andrew Yang (ay2546@columbia.edu)
- Tieqiong Zhang (tz2600@columbia.edu)
- Simon Billinge (sb2896@columbia.edu)

``scikit-package`` is developed by Billinge Group and its community contributors.

For a detailed list of contributors, see
https://github.com/scikit-package/scikit-package/graphs/contributors.

================
Acknowledgements
================

The Billinge Group's ``scikit-package`` has been modified from the NSLS-II scientific cookiecutter: https://github.com/nsls-ii/scientific-python-cookiecutter


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: GETTING STARTED

   overview

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: TUTORIALS

   tutorials/tutorial-level-1-2-3
   tutorials/tutorial-level-4
   tutorials/tutorial-level-5
   tutorials/tutorial-level-4-to-5
   tutorials/tutorial-level-5-migration
   tutorials/tutorial-manuscript

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: RELEASE GUIDES

   release-guides/pypi-github
   release-guides/conda-forge

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: EXAMPLES

   examples/overview
   examples/example-level-4
   examples/example-level-5
   examples/example-level-5-namespace
   examples/example-level-5-migration

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: PROGRAMMING GUIDES

   programming-guides/billinge-group-standards

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: SUPPORT

   support/frequently-asked-questions

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: REFERENCE

   release
   license




* :ref:`genindex`
