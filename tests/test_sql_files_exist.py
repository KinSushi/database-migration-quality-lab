from pathlib import Path


def test_required_sql_files_exist() -> None:
    root = Path(__file__).resolve().parents[1]
    required = [
        "00_legacy_schema.sql",
        "01_target_schema.sql",
        "02_seed_legacy_data.sql",
        "03_migration.sql",
        "04_validation_checks.sql",
        "05_reconciliation_report.sql",
        "06_performance_notes.sql",
    ]

    for filename in required:
        path = root / "sql" / filename
        assert path.exists(), f"Missing {filename}"
        assert path.read_text(encoding="utf-8").strip(), f"Empty {filename}"
