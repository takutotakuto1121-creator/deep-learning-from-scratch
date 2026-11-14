VENV 	= .venv
BIN 	= $(VENV)/bin
PIP 	= $(BIN)/pip
PYTHON 	= $(BIN)/python3
FLAKE8 	= $(BIN)/flake8
MYPY 	= $(BIN)/mypy
FLAGS	= --strict

.PHONY: install run run-ch01 run-ch02 clean fclean lint

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install -r requirements.txt

run: install
	$(PYTHON) -m src

run-ch01: install
	$(PYTHON) -m src.ch01

run-ch02: install
	$(PYTHON) -m src.ch02

run-ch03: install
	$(PYTHON) -m src.ch03

clean:
	find . -path ./$(VENV) -prune -o -name __pycache__ -type d -exec rm -rf {} +
	rm -rf .mypy_cache

fclean: clean
	rm -rf $(VENV)

lint: install
	$(FLAKE8) src
	$(MYPY) $(FLAGS) src