# Mapping Specification

| Legacy field | Target field | Rule |
|---|---|---|
| legacy_clients.client_ref | customers.customer_id | direct mapping |
| legacy_clients.segment_code | customers.customer_segment | RET=retail, PRM=premium, SME=sme |
| legacy_clients.domicile_country | customers.country | direct mapping |
| legacy_clients.created_date | customers.created_at | direct mapping |
| legacy_accounts.acct_ref | accounts.account_id | direct mapping |
| legacy_accounts.client_ref | accounts.customer_id | direct mapping |
| legacy_accounts.acct_type | accounts.account_type | CUR=current, SVG=savings |
| legacy_accounts.curr | accounts.currency | direct mapping |
| legacy_accounts.balance_chf | accounts.balance_chf | direct mapping |
