YARN := yarn --cwd=$(shell find . -maxdepth 2 -name frontend)

set_release = \
	find . -maxdepth 2 -name version.py -print0 | \
	xargs -0 sed -i "s/\(__release__ = \).*/\1$1/g"

install: dev
	$(YARN) install
	pip install -e .

upgrade: dev
	$(YARN) upgrade --latest
	pip install -e . --upgrade

run: dev
	$(YARN) start

build: release
	$(YARN) build
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

dev:
	$(call set_release,False)

release:
	$(call set_release,True)
