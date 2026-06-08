.PHONY: install test lint ci up down generate load-legacy migrate validate reconcile report reset clean

install:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

ci: lint test

up:
	docker compose up -d

down:
	docker compose down

generate:
	python -m migration_quality.generate_synthetic_legacy_data --output-dir data --clients 100 --accounts 220

load-legacy:
	python -m migration_quality.load_legacy

migrate:
	python -m migration_quality.migrate

validate:
	python -m migration_quality.validate

reconcile:
	python -m migration_quality.reconcile

report:
	python -m migration_quality.report

reset:
	docker compose down -v
	docker compose up -d
	python -m migration_quality.generate_synthetic_legacy_data --output-dir data --clients 100 --accounts 220
	python -m migration_quality.load_legacy
	python -m migration_quality.migrate
	python -m migration_quality.validate
	python -m migration_quality.reconcile
	python -m migration_quality.report

clean:
	rm -f data/*.csv
	rm -f reports/*.md reports/*.json
