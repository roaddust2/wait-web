PORT ?= 8000
ENV=poetry run
MANAGE=$(ENV) python3 manage.py

install:
	poetry install

lint:
	$(ENV) flake8 app

test:
	$(ENV) pytest

test-coverage:
	$(ENV) coverage run -m pytest tests
	$(ENV) coverage report --omit=*/tests/*,*/migrations/*
	$(ENV) coverage xml --omit=*/tests/*,*/migrations/*

makemessages:
	$(ENV) django-admin makemessages -l en
	$(ENV) django-admin makemessages -l ru

compilemessages:
	$(ENV) django-admin compilemessages

m_migrate:
	$(ENV) $(MANAGE) makemigrations

migrate:
	$(ENV) $(MANAGE) migrate

dev:
	$(MANAGE) runserver

prod:
	$(MANAGE) makemigrations
	$(MANAGE) migrate
	$(ENV) gunicorn -b 0.0.0.0:$(PORT) config.wsgi

secretkey:
	poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'