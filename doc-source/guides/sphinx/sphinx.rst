Introduction
************

Documentation:

- https://www.sphinx-doc.org/en/master/index.html

The Sphinx documentation is written using the
`reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html#footnotes>`__ *.rst* language (though it
can also be written with the `Markdown <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>`__ *.md*
language).

Getting started
***************

Root of the project:

..  code-block:: bash
    :emphasize-lines: 2, 3

    ../dir_tree/
        doc-source/...
        docs/...
        dir_tree/...
        .gitignore
        cli.py
        LICENSE
        make.bat
        Makefile
        README.md
        requirements.txt
        setup.py
        TODO.md

sphinx-autobuild
++++++++++++++++

Documentation:
- https://github.com/executablebooks/sphinx-autobuild

From the *root* folder, run the documentation on a local server which listens to any changes to the doc
and updates them live.

..  code-block:: bash
    :linenos:

    $ sphinx-autobuild doc-source/ docs/

.. important::
    *docs/* should be built with the previous commands, otherwise Github Pages won't be able to read the files
    properly. A *.nojekyll* file should also be added in the *docs/* folder if it is not already present.

sphinx-build
++++++++++++

Documentation:
- https://www.sphinx-doc.org/en/master/man/sphinx-build.html

From the *root* folder, run this command to simply build the documentation without listening to changes live.

..  code-block:: bash
    :linenos:

    $ sphinx-build doc-source/ docs/

.. important::
    *docs/* should be built with the previous commands, otherwise Github Pages won't be able to read the files
    properly. A *.nojekyll* file should also be added in the *docs/* folder if it is not already present.


sphinx-quickstart
+++++++++++++++++

Documentation:
- https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html

Sphinx themes
********************************************************************************

Switching themes
++++++++++++++++

To change the theme, simply change the value ``html_theme = "furo"`` *in conf.py* to any other theme.
You must also include the theme in your *setup.py*/*requirements.txt* files.

.. attention::
    Change links to actual images of the themes with links to repos/install procedure.

.. glossary::

    Book
        Can easily be converted to *.pdf* or *.rst*.

        - https://sphinx-themes.org/sample-sites/sphinx-book-theme/

    Furo
        Has light/dark mode.

        - https://sphinx-themes.org/sample-sites/furo/
        - https://pradyunsg.me/furo/customisation/logo/

    Groundwork
        Dark mode.

        - https://sphinx-themes.org/sample-sites/groundwork-sphinx-theme/

    Karma
        - https://sphinx-themes.org/sample-sites/karma-sphinx-theme/

    Press
        - https://sphinx-themes.org/sample-sites/sphinx-press-theme/

    Read The Docs
        - https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/
        - https://sphinx-rtd-theme.readthedocs.io/en/stable/

    Renku
        - https://sphinx-themes.org/sample-sites/renku-sphinx-theme/