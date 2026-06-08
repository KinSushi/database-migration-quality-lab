"""Synthetic legacy source data generator."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
import random


@dataclass(frozen=True)
class LegacyDataConfig:
    """Synthetic legacy data generation config."""

    clients: int = 100
    accounts: int = 220
    seed: int = 42


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def generate(config: LegacyDataConfig, output_dir: Path) -> None:
    """Generate synthetic legacy clients and accounts."""

    rng = random.Random(config.seed)
    today = date.today()
    countries = ["CH", "FR", "DE", "IT", "AT"]
    segments = ["RET", "PRM", "SME"]
    currencies = ["CHF", "EUR", "USD"]

    clients: list[dict[str, object]] = []
    for index in range(config.clients):
        clients.append(
            {
                "client_ref": f"LEG-CL-{index + 1:05d}",
                "segment_code": rng.choice(segments),
                "domicile_country": rng.choice(countries),
                "created_date": (today - timedelta(days=rng.randint(90, 2500))).isoformat(),
            }
        )

    accounts: list[dict[str, object]] = []
    for index in range(config.accounts):
        client = rng.choice(clients)
        balance = round(rng.lognormvariate(8.0, 1.1), 2)
        accounts.append(
            {
                "acct_ref": f"LEG-AC-{index + 1:06d}",
                "client_ref": client["client_ref"],
                "acct_type": rng.choice(["CUR", "SVG"]),
                "curr": rng.choice(currencies),
                "open_date": (today - timedelta(days=rng.randint(30, 2200))).isoformat(),
                "balance_chf": balance,
            }
        )

    _write_csv(output_dir / "legacy_clients.csv", clients)
    _write_csv(output_dir / "legacy_accounts.csv", accounts)


def parse_args() -> argparse.Namespace:
    """Parse CLI args."""

    parser = argparse.ArgumentParser(description="Generate synthetic legacy data.")
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--clients", type=int, default=100)
    parser.add_argument("--accounts", type=int, default=220)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> None:
    """CLI entrypoint."""

    args = parse_args()
    generate(LegacyDataConfig(args.clients, args.accounts, args.seed), Path(args.output_dir))
    print(f"Generated {args.clients} legacy clients and {args.accounts} legacy accounts")


if __name__ == "__main__":
    main()
