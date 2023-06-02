PORT=8000
ENV=poetry run
MANAGE=$(ENV) python3 manage.py

# Util commands
secretkey:
	poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

requirements.txt:
	$(ENV) pip freeze > requirements.txt

lint:
	$(ENV) flake8

test:
	$(ENV) pytest

test-coverage:
	$(ENV) coverage run -m pytest tests
	$(ENV) coverage report --omit=*/tests/*,*/migrations/*
	$(ENV) coverage xml --omit=*/tests/*,*/migrations/*

migprepare:
	$(MANAGE) makemigrations

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
	$(MANAGE) migrate

collectstatic:
	$(MANAGE) collectstatic --no-input

dev:
	$(MANAGE) runserver

start:
	$(ENV) gunicorn -b 0.0.0.0:$(PORT) config.wsgi

# Deploy commands
setup:
	source venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt
	pytnon3 manage.py migrate
	pytnon3 manage.py collectstatic --no-input