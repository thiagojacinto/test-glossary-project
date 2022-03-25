# docker hub user
DOCKER_HUB_USERNAME=thiagojacinto
DOCKER_HUB_REPOSITORY=test-glossary-api

# shell colors
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
	python -m pytest --verbose

lint: # use linter
	@echo "$(COLOUR_GREEN)Running lint process ...$(COLOUR_END)"
	python -m black $(APP_SOURCE_CODE_DIR) ; \
		python -m isort --profile black $(APP_SOURCE_CODE_DIR) ; \
		python -m autopep8 --in-place --recursive --verbose $(APP_SOURCE_CODE_DIR)

run: # starts uvicorn server with auto reload @ port 8880
	@echo "$(COLOUR_GREEN)Starting server ...$(COLOUR_END)"
	uvicorn testglossary.main:app --reload --port=8880

gh-deploy: # builds and deploy MkDocs documentation style to GitHub Pages
	mkdocs gh-deploy --verbose --strict --remote-branch="support/gh-pages"

docker-build: GET_NOW := $(shell date +%s)
docker-build: # builds a new container image
	@echo "$(COLOUR_RED)Building a Docker image ...$(COLOUR_END)"
	TAG_NAME="$(DOCKER_HUB_USERNAME)/$(DOCKER_HUB_REPOSITORY):$(GET_NOW)" ; \
	docker build -t $${TAG_NAME} . 

#: #########################################
#: #### Help - Makefile for TestGlossary API
#: #########################################

help: # list all Makefile commands
	@echo "$(COLOUR_BLUE)These are all the avalaible commands ...$(COLOUR_END)"
	grep ': #' Makefile