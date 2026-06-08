-- Source-vs-target client reconciliation
SELECT
    'clients_to_customers' AS reconciliation_name,
    (SELECT COUNT(*) FROM legacy_clients) AS source_count,
    (SELECT COUNT(*) FROM customers) AS target_count,
    (SELECT COUNT(*) FROM legacy_clients) - (SELECT COUNT(*) FROM customers) AS count_delta;

-- Source-vs-target account reconciliation
SELECT
    'accounts_to_accounts' AS reconciliation_name,
    (SELECT COUNT(*) FROM legacy_accounts) AS source_count,
    (SELECT COUNT(*) FROM accounts) AS target_count,
    (SELECT COUNT(*) FROM legacy_accounts) - (SELECT COUNT(*) FROM accounts) AS count_delta;

-- Balance reconciliation
SELECT
    'balance_reconciliation' AS reconciliation_name,
    ROUND((SELECT SUM(balance_chf) FROM legacy_accounts), 2) AS source_total,
    ROUND((SELECT SUM(balance_chf) FROM accounts), 2) AS target_total,
    ROUND((SELECT SUM(balance_chf) FROM legacy_accounts) - (SELECT SUM(balance_chf) FROM accounts), 2) AS amount_delta;
