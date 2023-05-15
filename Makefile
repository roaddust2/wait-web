PORT=8000
ENV=poetry run
MANAGE=$(ENV) python3 manage.py

# Util commands
secretkey:
	poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

requirements.txt: poetry.lock
	poetry export --format requirements.txt --output requirements.txt --without-hashes

lint:
	$(ENV) flake8

test:
	$(ENV) pytest

test-coverage:
	$(ENV) coverage run -m pytest tests
	$(ENV) coverage report --omit=*/tests/*,*/migrations/*
	$(ENV) coverage xml --omit=*/tests/*,*/migrations/*

migprepare:
	$(ENV) $(MANAGE) makemigrations

# Translation commands
# Need to have GNU gettext installed
transprepare:
	$(ENV) django-admin makemessages -l en
	$(ENV) django-admin makemessages -l ru
	$(ENV) django-admin makemessages -l tt

transcompile:
	$(ENV) django-admin compilemessages

# Main commands
install:
	poetry install

migrate:
	$(ENV) $(MANAGE) migrate

dev:
	$(MANAGE) runserver

start:
	$(ENV) gunicorn -b 0.0.0.0:$(PORT) config.wsgi