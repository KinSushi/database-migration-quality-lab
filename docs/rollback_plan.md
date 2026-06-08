# Rollback Plan

## Purpose

This rollback plan documents how to reset the synthetic local migration lab.

## Automated rollback

```bash
make reset
```

## Manual rollback

```bash
docker compose down -v
docker compose up -d
make generate
make load-legacy
make migrate
make validate
make reconcile
```

## Public-safety note

This is not a production rollback procedure. It is a synthetic portfolio artifact.
