"""Validation checks for migrated data."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from migration_quality.config import Settings, load_settings
from migration_quality.db import connect


@dataclass(frozen=True)
class ValidationCheck:
    check_id: str
    check_name: str
    query: str


@dataclass(frozen=True)
class ValidationResult:
    check_id: str
    check_name: str
    status: str
    failed_rows: int


def get_validation_checks() -> list[ValidationCheck]:
    """Return validation checks."""

    return [
        ValidationCheck(
            "VAL-001",
            "orphan_accounts",
            """
            SELECT COUNT(*)
            FROM accounts a
            LEFT JOIN customers c ON a.customer_id = c.customer_id
            WHERE c.customer_id IS NULL
            """,
        ),
        ValidationCheck(
            "VAL-002",
            "negative_balances",
            "SELECT COUNT(*) FROM accounts WHERE balance_chf < 0",
        ),
        ValidationCheck(
            "VAL-003",
            "unknown_segments",
            "SELECT COUNT(*) FROM customers WHERE customer_segment = 'unknown'",
        ),
        ValidationCheck(
            "VAL-004",
            "invalid_account_types",
            "SELECT COUNT(*) FROM accounts WHERE account_type NOT IN ('current', 'savings', 'other')",
        ),
    ]


def run_validation(settings: Settings | None = None) -> list[ValidationResult]:
    """Run validations and persist results."""

    runtime = settings or load_settings()
    executed_at = datetime.now(UTC)
    results: list[ValidationResult] = []
    with connect(runtime) as connection:
        with connection.cursor() as cursor:
            for check in get_validation_checks():
                cursor.execute(check.query)
                failed_rows = int(cursor.fetchone()[0])
                result = ValidationResult(
                    check.check_id,
                    check.check_name,
                    "PASS" if failed_rows == 0 else "FAIL",
                    failed_rows,
                )
                results.append(result)
                cursor.execute(
                    """
                    INSERT INTO validation_results (check_id, check_name, status, failed_rows, executed_at)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (check_id)
                    DO UPDATE SET
                        check_name = EXCLUDED.check_name,
                        status = EXCLUDED.status,
                        failed_rows = EXCLUDED.failed_rows,
                        executed_at = EXCLUDED.executed_at
                    """,
                    (result.check_id, result.check_name, result.status, result.failed_rows, executed_at),
                )
        connection.commit()
    return results


def main() -> None:
    """CLI entrypoint."""

    for result in run_validation():
        print(f"{result.check_id} | {result.status} | {result.check_name} | failed={result.failed_rows}")


if __name__ == "__main__":
    main()
