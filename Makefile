.PHONY: test
test:
	pytest tests -svv --log-cli-level=DEBUG

install/dev:
	pip install -e .'[dev]'

install:
	pip install .'[server]'

lint/vulture:
	vulture jobs_searcher --min-confidence 80
	vulture tests --min-confidence 80

lint/black: ## check style with black
	black --check jobs_searcher tests

lint/typing:
	mypy jobs_searcher

lint: lint/black lint/vulture lint/typing ## check style

run:
	streamlit run streamlit_app.py

clean: clean-build clean-pyc clean-test clean-vim ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -fr .mypy_cache

clean-vim: ## remove .sw* files
	find . -type f -name "*.sw[klmnop]" -delete

