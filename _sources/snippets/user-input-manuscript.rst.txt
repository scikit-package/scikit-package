  .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Prompt
        - Description and example
      * - project_name
        - The name displayed in the ``README.rst``.
          Use ``name-with-hyphens`` e.g., ``my-manuscript``.
      * - journal_template
        - Specifies which journal template to use to create the manuscript.
	  The default value is ``[1]``, which corresponds to the ``article`` template.
      * - user_latex_repo_url
        - The URL to the GitHub repository where the LaTeX files are located. Files with the specified names will be parsed, and the other files will be copied directly into the manuscript folder.
          e.g., ``https://github.com/scikit-package/default-latex-headers.git``
