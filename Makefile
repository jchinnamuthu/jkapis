.PHONY: test build upload

test:
	pytest tests/

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*
