ifneq (,$(wildcard ./real_estate/.env))
include ./real_estate/.env
export
ENV_FILE_PARAM = --env-file ./real_estate/.env
endif

# Variables (optional)
PYTHON=python3
MANAGE=python3 manage.py

# Virtual environment activation (if you use one)
venv:
	venv\Scripts\activate

# Run Django development server
run:
	$(MANAGE) runserver

build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d

down:
	docker compose down

show-logs:
	docker compose logs

migrate:
	docker compose exec api python manage.py migrate

makemigrations:
	docker compose exec api python manage.py makemigrations

superuser:
	docker compose exec api python manage.py createsuperuser

collectstatic:
	docker compose exec api python manage.py collectstatic --no-input --clear

down-v:
	docker compose down -v

volume:
	docker volume inspect estate-src_postgres_data

estate-db:
	docker compose exec postgres-db psql --username=postgres --dbname=real_estate

test:
	docker compose exec api pytest -p no:warnings --cov=.

test-html:
	docker compose exec api pytest -p no:warnings --cov=. --cov-report html

flake8:
	docker compose exec api flake8 .

black-check:
	docker compose exec api black --check --exclude=migrations .

black-diff:
	docker compose exec api black --diff --exclude=migrations .

isort-check:
	docker compose exec api isort . --check-only --skip env --skip migrations

isort-diff:
	docker compose exec api isort . --diff --skip env --skip migrations

isort:
	docker compose exec api isort . --skip env --skip migrations




 