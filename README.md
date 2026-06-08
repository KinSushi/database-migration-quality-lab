# database-migration-quality-lab

<div align="center">

<img src="assets/database-migration-banner.svg" alt="database-migration-quality-lab banner" width="100%"/>

<br/>

**Legacy-to-target data migration lab with SQL validation, reconciliation and rollback documentation**

PostgreSQL · SQL · Python · Data Quality · Migration · Reconciliation · Rollback

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Migration%20%2F%20Validation-003B57?style=flat)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Data Quality](https://img.shields.io/badge/Data%20Quality-Reconciliation-2EA043?style=flat)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![Public Safety](https://img.shields.io/badge/Data-Synthetic%20Only-24292F?style=flat)

</div>

---

## Executive summary

`database-migration-quality-lab` is a public technical portfolio project demonstrating how to migrate synthetic legacy financial-style data into a target normalized schema, validate the migration and generate reconciliation evidence.

```text
legacy schema -> synthetic source data -> migration SQL -> target schema -> validation checks -> reconciliation report -> rollback plan
```

The project is designed for regulated and data-intensive environments: banks, insurers, health insurers, reinsurance, financial infrastructure, consulting, data-platform teams and legacy-to-modern transformation programs.

No real banking, insurance, health, client, employer or private data belongs here.

---

## Target roles

| Role family | Why this project helps |
|---|---|
| Junior Data Engineer | relational schema, SQL migration, Python automation |
| Data Migration Engineer | source-to-target mapping, validation, reconciliation |
| Database / Data Quality Analyst | controls, row counts, balance checks, referential integrity |
| Application & Data Support | incident triage and rollback documentation |
| Core banking / insurance IT | legacy-to-modern data handling and auditability |
| Consulting / integration | migration strategy, handover and evidence pack |

---

## Architecture

```mermaid
flowchart LR
    A[Synthetic legacy data generator] --> B[legacy_clients / legacy_accounts]
    B --> C[Migration SQL]
    C --> D[customers / accounts]
    D --> E[Validation checks]
    D --> F[Reconciliation report]
    E --> G[validation_results]
    F --> H[reconciliation_results]
    G --> I[Markdown report]
    H --> I
    I --> J[Rollback plan]
```

---

## Quickstart

```bash
make install
make generate
make test
make lint
```

With Docker / PostgreSQL:

```bash
make up
make load-legacy
make migrate
make validate
make reconcile
make report
```

Reset local environment:

```bash
make reset
```

---

## Repository structure

```text
database-migration-quality-lab/
├── README.md
├── PORTFOLIO.md
├── LICENSE
├── .gitignore
├── .env.example
├── pyproject.toml
├── Makefile
├── docker-compose.yml
├── assets/
│   └── database-migration-banner.svg
├── .github/workflows/ci.yml
├── data/
├── sql/
├── src/migration_quality/
├── tests/
├── docs/
├── reports/
└── output/
```

---

## Public-safety rules

- synthetic data only;
- no real bank, insurance, health, client, employer or private data;
- no production migration claims;
- no secrets or private infrastructure identifiers;
- no CVs, cover letters, job trackers or salary targets.

---

## Portfolio signal

This repository proves the ability to reason about legacy-to-target migration, SQL validation, reconciliation, rollback and documentation in regulated-data environments.
