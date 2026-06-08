"""Load legacy synthetic CSV files into PostgreSQL."""

from __future__ import annotations

import csv
from pathlib import Path

from migration_quality.config import Settings, load_settings
from migration_quality.db import connect, execute_sql_file

ROOT = Path(__file__).resolve().parents[2]
SQL_DIR = ROOT / "sql"


def _copy_csv(table_name: str, csv_path: Path, settings: Settings) -> int:
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing CSV file: {csv_path}")
    with csv_path.open("r", encoding="utf-8", newline="") as file:
        row_count = sum(1 for _ in csv.DictReader(file))
    with connect(settings) as connection:
        with connection.cursor() as cursor:
            with csv_path.open("r", encoding="utf-8") as file:
                with cursor.copy(f"COPY {table_name} FROM STDIN WITH CSV HEADER") as copy:
                    for line in file:
                        copy.write(line)
        connection.commit()
    return row_count


def load_legacy(settings: Settings | None = None) -> dict[str, int]:
    """Create legacy schema and load CSV files."""

    runtime = settings or load_settings()
    execute_sql_file(SQL_DIR / "00_legacy_schema.sql", runtime)
    execute_sql_file(SQL_DIR / "01_target_schema.sql", runtime)
    with connect(runtime) as connection:
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE legacy_accounts, legacy_clients RESTART IDENTITY CASCADE")
        connection.commit()
    return {
        "legacy_clients": _copy_csv("legacy_clients", runtime.data_dir / "legacy_clients.csv", runtime),
        "legacy_accounts": _copy_csv("legacy_accounts", runtime.data_dir / "legacy_accounts.csv", runtime),
    }


def main() -> None:
    """CLI entrypoint."""

    for table, rows in load_legacy().items():
        print(f"{table}: loaded={rows}")


if __name__ == "__main__":
    main()
