PYTHON := .venv/bin/python3

.PHONY: test

test:
	$(PYTHON) -m pytest

run:
	python3 -m music_audit $(DIR)