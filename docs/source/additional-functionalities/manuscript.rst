.. _scikit-package-manuscript-tutorials:

Create a configured LaTeX manuscript folder with ``scikit-package``
===================================================================

Overview
--------

This is a tutorial for using ``scikit-package`` to create a configured manuscript folder by running the command

   .. code-block:: bash

	package create manuscript

We strongly recommend that you read through :ref:`manuscript-customize-latex-repo` to unleash the full potential of creating a manuscript folder with ``scikit-package``.

Prerequisites
^^^^^^^^^^^^^^

To proceed with the following steps, we assume that you

#. know how to use ``conda`` to create an environment and install ``scikit-package`` in the environment. Please see :ref:`conda-env-setup-simple` for more information.
#. (Optional) know how to manage repositories on GitHub. Please see the GitHub tutorial `GitHub Hello World <https://docs.github.com/en/get-started/start-your-journey/hello-world>`_ for more information.

.. _manuscript-run-the-command:

Create a manuscript folder with minimum setup.
---------------------------------------------------------------
#. Create a ``conda`` environment with ``scikit-package`` installed and activate the environment. Please see :ref:`conda-env-setup-simple` for more information.

   .. code-block:: bash

	conda create -n <project-name>-env scikit-package
	conda activate <project-name>-env

#. Go to the path where the manuscript folder will be created.

   .. code-block:: bash

	cd <manuscript-folder-parent-folder>

#. Run the command.

   .. code-block:: bash

	package create manuscript

2. Answer the following questions:

    .. include:: ../snippets/user-input-manuscript.rst

    .. note::

        You may press the "Enter" key to accept the default values for the questions.

3. Done! A manuscript folder named ``<project_name>`` is created inside ``<manuscript-folder-parent-folder>``.

.. _manuscript-customize-latex-repo:

(Recommended) Customize the your LaTeX repositories
---------------------------------------------------

The flexibility of using ``package create manuscript`` to create a manuscript folder is the ability to customize LaTeX repositories for different manuscripts. The following steps will help you create a LaTeX repository to be used by ``package create manuscript``.

Example
^^^^^^^

#. Create a GitHub repository. Please see :ref:`create-new-github-repo` for more information. As an example, set ``Repository name`` to be ``my-latex-repo-example``, choose the visibility to be ``public``, and select ``None`` for ``.gitignore`` and ``license``. You will be directed to the ``my-latex-repo-example`` page in GitHub after it is created.

#. Find the ``Quick setup`` section in the ``my-latex-repo-example`` page, choose the ``HTTPS`` option and copy the URL in the section. The URL will be referred to as ``<copied-my-latex-repo-example-url>`` in the following steps.

#. Open the terminal and clone the ``my-latex-repo-example`` repository. After the command, a ``my-latex-repo-example`` folder will be created locally.

   .. code-block:: bash

        cd ~
	git clone <copied-my-latex-repo-example-url>

#. Create ``usepackages.txt`` and ``newcommands.txt`` inside the ``~/my-latex-repo-example`` directory.

    ``usepackages.txt`` is used to import packages using ``\usepackage{graphicx}`` into the main LaTeX file. ``newcommands.txt`` is used to add commands like ``\newcommand{\a_command}[1]{\mathrm{#1}}`` into the main LaTeX file. The main LaTeX file is ``manuscript.tex`` in the manuscript folder by default.

   .. note::
      No LaTeX syntax check is executed during ``package create manuscript``. The content in ``usepackages.txt`` will be inserted after ``\documentclass`` and the content in ``newcommands.txt`` will be inserted after all ``\usepackage`` commands.

   Example of ``usepackages.txt``

   .. code-block:: text

	\usepackage{mathtools}
	\usepackage{amsmath}
	\usepackage{mathtools}
	...

   Example of ``newcommands.txt``

   .. code-block:: text

	\newcommand{\command_1}[1]{\mathrm{#1}}
	\newcommand{\command_2}[1]{\mathbb{#1}}
	\newcommand{\command_3}[1]{\mathcal{#1}}
	...


#. You can also add any additional files inside the ``~/my-latex-repo-example`` folder. These are the files that will be copied directly into the manuscript folder. e.g.

   .. code-block:: bash

	cd ~/my-latex-repo-example
	touch my-class-file.cls
	touch my-style-file.sty
	touch my-bib-file.bib


#. Commit the change and sync the ``my-latex-repo-example`` repository in GitHub.

   .. code-block:: bash

	git add .
	git commit -m 'skpkg: initialize a LaTeX repository'
	git push origin main

#. Done! To test it, go to the path where a manuscript folder will be created and run ``package create manuscript`` with ``<copied-my-latex-example-url>`` as the input for ``<user_latex_repo_url>``.

   .. code-block:: bash

	mkdir ~/my-manuscripts
	cd ~/my-manuscripts
	package create manuscript

A manuscript folder will be created in the ``~/my-manuscripts``. Files from the ``my-latex-repo-example`` GitHub repo will be copied into the manuscript folder. Packages and commands in ``usepackages.txt`` and ``newcommands.txt`` will be inserted after ``\documentclass`` in the main LaTeX file (``manuscript.tex`` by default) in the manuscript folder. The names of all ``.bib``  will be added to the ``\bibliography`` entry in the main LaTeX file.

In this example, we used a GitHub repository named ``my-latex-repo-example`` to store the LaTeX files. The repository is maintained locally in ``~/my-latex-repo-example`` and five files ``my-class-file.cls``, ``my-style-file.sty``, ``my-bib-file.bib``, ``usepackages.txt`` and ``newcommands.txt`` are created inside ``my-latex-repo-example``. The name for the repository and its local location can be chosen freely. You can also add, remove, or modify any files in that repository.

Want a new manuscript template?
----------------------------------------------------------------------

Feel free to contribute it! You are welcome to create issues and PRs in `scikit-package-manuscript <https://github.com/scikit-package/scikit-package-manuscript>`_.
