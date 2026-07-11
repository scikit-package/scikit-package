**Added:**

* Add a ``use_codecov`` cookiecutter prompt (default ``No``) so Codecov is optional at package create time.

**Changed:**

* Default new Level 5 packages to the no-Codecov CI workflows
  (``_tests-on-pr-no-codecov.yml`` and ``_matrix-no-codecov-on-merge-to-main.yml``),
  omit the ``CODECOV_TOKEN`` secret, and skip shipping ``.codecov.yml`` unless
  the user chooses ``use_codecov: Yes``.

**Deprecated:**

* <news item>

**Removed:**

* <news item>

**Fixed:**

* <news item>

**Security:**

* <news item>
