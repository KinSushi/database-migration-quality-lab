"""Generate a markdown migration quality report."""

from __future__ import annotations

from datetime import UTC, datetime

import pandas as pd

from migration_quality.config import load_settings
from migration_quality.db import fetch_dataframe


def dataframe_to_markdown(frame: pd.DataFrame) -> str:
    """Render a DataFrame as a small markdown table without optional dependencies."""

    if frame.empty:
        return "No rows."
    columns = [str(column) for column in frame.columns]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in frame.iterrows():
        values = [str(row[column]) for column in frame.columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def generate_report_markdown() -> str:
    """Generate markdown report from validation and reconciliation result tables."""

    validations = fetch_dataframe("SELECT * FROM validation_results ORDER BY check_id")
    reconciliations = fetch_dataframe(
        "SELECT * FROM reconciliation_results ORDER BY executed_at DESC LIMIT 10"
    )

    lines = [
        "# Migration Quality Report",
        "",
        f"Generated at: {datetime.now(UTC).isoformat()}",
        "",
        "## Validation results",
        "",
        dataframe_to_markdown(validations),
        "",
        "## Reconciliation results",
        "",
        dataframe_to_markdown(reconciliations),
        "",
        "## Public-safety note",
        "",
        "Synthetic data only. No real client, bank, insurance, health, employer or private data.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """CLI entrypoint."""

    settings = load_settings()
    settings.report_dir.mkdir(parents=True, exist_ok=True)
    path = settings.report_dir / "migration_quality_report.md"
    path.write_text(generate_report_markdown(), encoding="utf-8")
    print(f"Report written to {path}")


if __name__ == "__main__":
    main()
