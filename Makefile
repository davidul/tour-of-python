venv-3.12:
	/Users/david/.pyenv/versions/3.12.1/bin/python -m venv venv-3.12

build:
	docker build -t touf-of-python .

flake:
	docker run --rm -v $(shell pwd):/app tour-of-python flake8 /app

mypy:
	docker run --rm -v $(shell pwd):/data cytopia/mypy /data

black:
	docker run --rm -v $(shell pwd):/app tour-of-python python3 -m black /app

exec:
	docker run --rm -v $(shell pwd):/app tour-of-python python3 /app/01-strings/01-string.py