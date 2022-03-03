# Welcome to TestGlossary projects

This project uses mkdocs. For full documentation how-to visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `make install`    - install project dependencies from requirements.txt file
* `make test`       -  execute all tests
* `make lint`       - use linter
* `make help`       - lists all Makefile commands

## Project layout

    Makefile      # Makefile with simplifications for project maintenance
    mkdocs.yml    # MkDocs configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other documentation related files.
    tests/
        ...       # Test related files should be here
    testglossary/
        ...       # Main application files must be placed under this directory, following futher structure.

