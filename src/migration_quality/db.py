"""Database helpers."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import psycopg

from migration_quality.config import Settings, load_settings


def connect(settings: Settings | None = None) -> psycopg.Connection:
    """Open PostgreSQL connection."""

    return psycopg.connect((settings or load_settings()).dsn)


def split_sql_statements(sql_text: str) -> list[str]:
    """Split simple SQL files into executable statements."""

    return [statement.strip() for statement in sql_text.split(";") if statement.strip()]


def execute_sql_file(path: Path, settings: Settings | None = None) -> None:
    """Execute all statements from SQL file."""

    with connect(settings) as connection:
        with connection.cursor() as cursor:
            for statement in split_sql_statements(path.read_text(encoding="utf-8")):
                cursor.execute(statement)
        connection.commit()


def fetch_dataframe(query: str, settings: Settings | None = None) -> pd.DataFrame:
    """Fetch query as pandas DataFrame."""

    with connect(settings) as connection:
        return pd.read_sql_query(query, connection)


def reset_target_tables(settings: Settings | None = None) -> None:
    """Reset target/result tables."""

    with connect(settings) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                TRUNCATE TABLE reconciliation_results, validation_results, accounts, customers
                RESTART IDENTITY CASCADE
                """
            )
        connection.commit()
