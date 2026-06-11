PYTHON := .venv/bin/python3

.PHONY: test

test:
	$(PYTHON) -m pytest

run:
	$(PYTHON) -m music_audit $(DIR)