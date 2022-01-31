install:
		pip install --upgrade pip && pip install -r requirements.txt

test:
		pytest --cov=hello -vv

format:
		black *.py

lint:
		pylint --disable=R,C hello.py

all: install lint test format