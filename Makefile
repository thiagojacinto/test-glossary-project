COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m

# setting source code directory
APP_SOURCE_CODE_DIR='./testglossary'

install: # install project dependencies from requirements.txt file
	@echo "$(COLOUR_RED)Start installing process ...$(COLOUR_END)"
	pip install -r ./requirements.txt	

test: # execute all tests
	@echo "$(COLOUR_GREEN)Executing tests ...$(COLOUR_END)"
	python -m pytest

lint: # use linter
	@echo "$(COLOUR_GREEN)Running lint process ...$(COLOUR_END)"
	python -m black $(APP_SOURCE_CODE_DIR) ; \
		python -m isort --profile black $(APP_SOURCE_CODE_DIR) ; \
		python -m autopep8 $(APP_SOURCE_CODE_DIR)

help: # list all Makefile commands
	@echo "$(COLOUR_BLUE)These are all the avalaible commands ...$(COLOUR_END)"
	grep ':' Makefile

