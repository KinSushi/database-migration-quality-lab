"""Run target schema migration."""

from __future__ import annotations

from pathlib import Path

from migration_quality.config import Settings, load_settings
from migration_quality.db import execute_sql_file, reset_target_tables

ROOT = Path(__file__).resolve().parents[2]
SQL_DIR = ROOT / "sql"


def migrate(settings: Settings | None = None) -> None:
    """Run migration from legacy tables into target tables."""

    runtime = settings or load_settings()
    execute_sql_file(SQL_DIR / "01_target_schema.sql", runtime)
    reset_target_tables(runtime)
    execute_sql_file(SQL_DIR / "03_migration.sql", runtime)


def main() -> None:
    """CLI entrypoint."""

    migrate()
    print("Migration completed")


if __name__ == "__main__":
    main()
