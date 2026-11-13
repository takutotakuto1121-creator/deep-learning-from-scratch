VENV 	= .venv
BIN 	= $(VENV)/bin
PIP 	= $(BIN)/pip
PYTHON 	= $(BIN)/python3
FLAKE8 	= $(BIN)/flake8
MYPY 	= $(BIN)/mypy
FLAGS	= --strict

.PHONY: install run debug lint lint-strict

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install -r requirements.txt

run-ch01: install
	$(PYTHON) -m ch01

run-ch02: install
	$(PYTHON) -m ch02

clean:
	rm -rf */__pycache__
	rm -rf .mypy_cache

fclean: clean
	rm -rf $(VENV)

lint: install
	$(FLAKE8) src
	$(MYPY) $(FLAGS) src