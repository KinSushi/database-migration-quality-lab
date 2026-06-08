from pathlib import Path

import pandas as pd

from migration_quality.generate_synthetic_legacy_data import LegacyDataConfig, generate


def test_generate_synthetic_legacy_data(tmp_path: Path) -> None:
    generate(LegacyDataConfig(clients=5, accounts=12), tmp_path)

    clients = pd.read_csv(tmp_path / "legacy_clients.csv")
    accounts = pd.read_csv(tmp_path / "legacy_accounts.csv")

    assert len(clients) == 5
    assert len(accounts) == 12
    assert set(clients.columns) == {"client_ref", "segment_code", "domicile_country", "created_date"}
    assert "balance_chf" in accounts.columns
