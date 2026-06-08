# Data Dictionary

## Legacy tables

| Table | Column | Description |
|---|---|---|
| legacy_clients | client_ref | Synthetic legacy client key |
| legacy_clients | segment_code | RET, PRM or SME |
| legacy_clients | domicile_country | Synthetic country |
| legacy_accounts | acct_ref | Synthetic legacy account key |
| legacy_accounts | client_ref | Synthetic legacy client key |
| legacy_accounts | acct_type | CUR or SVG |
| legacy_accounts | curr | CHF, EUR or USD |
| legacy_accounts | balance_chf | Synthetic account balance |

## Target tables

| Table | Column | Description |
|---|---|---|
| customers | customer_id | Target customer key |
| customers | customer_segment | retail, premium, sme or unknown |
| accounts | account_id | Target account key |
| accounts | customer_id | Target customer reference |
| accounts | account_type | current, savings or other |
| accounts | balance_chf | Migrated synthetic balance |
