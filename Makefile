PY_VERSION := 3.10

virtual-env:	## Setup Virtual Environment
	virtualenv --python=python${PY_VERSION} venv

install-dev:	## Install development dependencies
	pip install -r requirements.txt

lint:		## Run lint checks
	mypy --implicit-reexport app/
	flake8 app/ tests
	black app/ tests --line-length 120 --check

test: lint	## Run lint checks and unit tests
	pytest --durations=5 --cov=app/ -vv \
	 --cov-report term \
	 --cov-report html:./reports/coverage/unit_test_coverage_html \
	 --cov-report xml:./reports/coverage/unit_test_coverage.xml \
	 --cov-fail-under 100

format:		## Format code according to lint checks
	black --line-length 120 app/ tests

start-app:  ## Run flask app in docker container
	docker build -t image_edges_api ./
	docker run -p 8888:8888 image_edges_api