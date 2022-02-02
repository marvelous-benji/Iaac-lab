install:
		pip install --upgrade pip && pip install -r requirements.txt

test:
		pytest --cov=hello --cov=greeting --cov=web -vv tests

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

static-check:
		mypy  *.py tests/

all: install lint test format
