# Validation

## Purpose

This file documents the local and CI validation path for this repository.

## Static validation

```powershell
python -m compileall -q src tests
python -m pytest -q --maxfail=1
python -m ruff check .
```

## Migration execution checks

```powershell
python -m migration_quality.generate_synthetic_legacy_data --output-dir data --clients 5 --accounts 10
python -m migration_quality.validate
python -m migration_quality.reconcile
```

Database-backed commands require PostgreSQL through Docker Compose:

```powershell
docker compose up -d
python -m migration_quality.load_legacy
python -m migration_quality.migrate
python -m migration_quality.validate
python -m migration_quality.reconcile
python -m migration_quality.report
```

## Observed local validation evidence

A local PowerShell validation log showed the following successful outputs for this repository:

```text
pytest: 5 passed
ruff: All checks passed!
generate_synthetic_legacy_data: Generated 5 legacy clients and 10 legacy accounts
```

## Public-safety validation

```powershell
Get-ChildItem -Recurse -File |
  Where-Object { $_.FullName -notmatch "\\.git\\" -and $_.FullName -notmatch "\\.venv\\" } |
  Select-String -Pattern "BEGIN .*PRIVATE KEY","gho_","api_key","secret","token","password"
```

Expected review notes:

- `.env.example` may contain local placeholder names.
- `.gitignore` and documentation may contain safety words such as `secret` or `password`.
- Real credentials must never appear.

## Portfolio rule

This repository is public technical evidence. It must not contain CVs, cover letters, salary targets, private school documents, real client data, employer data, credentials or production decisioning claims.
