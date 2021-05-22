FRONTEND = $(shell find . -maxdepth 2 -name frontend)

install:
	yarn --cwd=$(FRONTEND) install
	pip install -e .

upgrade:
	yarn --cwd=$(FRONTEND) upgrade --latest
	pip install -e . --upgrade

build:
	yarn --cwd=$(FRONTEND) build
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*
