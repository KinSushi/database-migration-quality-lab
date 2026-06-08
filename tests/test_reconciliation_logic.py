from decimal import Decimal

from migration_quality.reconcile import ReconciliationResult


def test_reconciliation_result_shape() -> None:
    result = ReconciliationResult(
        reconciliation_name="balance_reconciliation",
        source_count=None,
        target_count=None,
        count_delta=None,
        source_total=Decimal("100.00"),
        target_total=Decimal("100.00"),
        amount_delta=Decimal("0.00"),
    )

    assert result.reconciliation_name == "balance_reconciliation"
    assert result.amount_delta == Decimal("0.00")
