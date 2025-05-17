To ignore a word, add it to ``.codespell/ignore_words.txt``. You can find an example file here: https://github.com/diffpy/diffpy.fourigui/blob/main/.codespell/ignore_words.txt.

To ignore a specific line, add it to ``.codespell/ignore_lines.txt``. See an example below:

.. code-block:: text

  ;; src/translation.py
  ;; The following single-line comment is written in German.
  # Hallo Welt

To ignore a specific file extension, add ``*.ext`` to the ``skip`` section under ``[tool.codespell]`` in ``pyproject.toml``. You can find an example file here: https://github.com/diffpy/diffpy.fourigui/blob/main//pyproject.toml.
