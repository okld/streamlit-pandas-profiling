YARN := yarn --cwd=$(shell find . -maxdepth 2 -name frontend)

set_release = \
	find . -maxdepth 2 -name version.py -print0 | \
	xargs -0 sed -i "s/\(__release__ = \).*/\1$1/g"

.PHONY: install
install: dev
	$(YARN) install
	pip install -e .

.PHONY: upgrade
upgrade: dev
	$(YARN) upgrade --latest
	pip install -e . --upgrade

.PHONY: run
run: dev
	$(YARN) start

.PHONY: build
build: release
	$(YARN) build
	python setup.py sdist bdist_wheel

.PHONY: upload
upload:
	twine upload dist/*

.PHONY: dev
dev:
	$(call set_release,False)

.PHONY: release
release:
	$(call set_release,True)
