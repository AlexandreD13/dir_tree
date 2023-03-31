Installing
==========

To use Dir_tree, you need to add it to your PATH. Go to the root of Dir_tree
(where **setup.py** is):

..  code-block:: bash
    :emphasize-lines: 9

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

and run:

..  code-block:: bash

    $ python setup.py build

    $ python setup.py install