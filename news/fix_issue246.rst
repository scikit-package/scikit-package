**Added:**

* <news item>

**Changed:**

* Launch ``cookiecutter`` as ``python -m cookiecutter`` in ``package create`` so it no longer depends on a ``cookiecutter`` executable or ``.bat`` shim being on the Windows ``PATH``.
* Read and write text files with an explicit ``utf-8`` encoding instead of the platform default, which is ``cp1252`` on Windows and failed on non-ASCII content such as author names.

**Deprecated:**

* <news item>

**Removed:**

* <news item>

**Fixed:**

* Quote the pull request title in ``package update conda-forge`` with double quotes. Single quotes are not quote characters in the Windows ``cmd.exe`` shell, so ``gh pr create`` received a split title and failed.

**Security:**

* <news item>
