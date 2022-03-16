# Welcome to TestGlossary

This is the official documentation for the TestGlossary project.

If you have ideas, feel free to get in touch or open an Issue to the project [repository](https://github.com/thiagojacinto/test-glossary-project/issues).

## Commands

* `make run`        - start uvicorn server at port `8880`
* `make install`    - install project dependencies from requirements.txt file
* `make test`       - execute all tests
* `make lint`       - use linter
* `make lint`       - use linter
* `make help`       - lists all Makefile commands

### Auxiliary commands
* `make gh-deploy`      - uses the built-in tool of MkDocs (docs [here](https://www.mkdocs.org/user-guide/deploying-your-docs/)) to deploy documenation to the specific branch that is responsible to handle the GitHub page: [thiagojacinto.github.io/test-glossary-project/](https://thiagojacinto.github.io/test-glossary-project/)
* `make docker-build`   - build a new Docker image and tag it with timestamp.

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

## Why documentation?

Documentation matters.

To help with this project goal, TestGlossary uses MkDocs. For full documentation how-to visit [mkdocs.org](https://www.mkdocs.org). We `highly` recommend you to.