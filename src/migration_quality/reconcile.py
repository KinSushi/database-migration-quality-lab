"""Reconciliation reporting for migration quality."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from uuid import uuid4

from migration_quality.config import Settings, load_settings
from migration_quality.db import connect


@dataclass(frozen=True)
class ReconciliationResult:
    reconciliation_name: str
    source_count: int | None
    target_count: int | None
    count_delta: int | None
    source_total: Decimal | None = None
    target_total: Decimal | None = None
    amount_delta: Decimal | None = None


def run_reconciliation(settings: Settings | None = None) -> list[ReconciliationResult]:
    """Run source-target reconciliation checks."""

    runtime = settings or load_settings()
    results: list[ReconciliationResult] = []
    with connect(runtime) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM legacy_clients")
            source_clients = int(cursor.fetchone()[0])
            cursor.execute("SELECT COUNT(*) FROM customers")
            target_customers = int(cursor.fetchone()[0])
            results.append(
                ReconciliationResult(
                    "clients_to_customers",
                    source_clients,
                    target_customers,
                    source_clients - target_customers,
                )
            )

            cursor.execute("SELECT COUNT(*) FROM legacy_accounts")
            source_accounts = int(cursor.fetchone()[0])
            cursor.execute("SELECT COUNT(*) FROM accounts")
            target_accounts = int(cursor.fetchone()[0])
            results.append(
                ReconciliationResult(
                    "accounts_to_accounts",
                    source_accounts,
                    target_accounts,
                    source_accounts - target_accounts,
                )
            )

            cursor.execute("SELECT ROUND(SUM(balance_chf), 2) FROM legacy_accounts")
            source_total = cursor.fetchone()[0] or Decimal("0.00")
            cursor.execute("SELECT ROUND(SUM(balance_chf), 2) FROM accounts")
            target_total = cursor.fetchone()[0] or Decimal("0.00")
            results.append(
                ReconciliationResult(
                    "balance_reconciliation",
                    None,
                    None,
                    None,
                    source_total,
                    target_total,
                    source_total - target_total,
                )
            )

            for result in results:
                cursor.execute(
                    """
                    INSERT INTO reconciliation_results
                        (reconciliation_id, reconciliation_name, source_count, target_count,
                         count_delta, source_total, target_total, amount_delta)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        f"REC-{uuid4().hex[:12].upper()}",
                        result.reconciliation_name,
                        result.source_count,
                        result.target_count,
                        result.count_delta,
                        result.source_total,
                        result.target_total,
                        result.amount_delta,
                    ),
                )
        connection.commit()
    return results


def main() -> None:
    """CLI entrypoint."""

    for result in run_reconciliation():
        print(result)


if __name__ == "__main__":
    main()
