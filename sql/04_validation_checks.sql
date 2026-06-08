-- VAL-001 target customers count
SELECT 'customers_row_count' AS check_name, COUNT(*) AS target_count
FROM customers;

-- VAL-002 target accounts count
SELECT 'accounts_row_count' AS check_name, COUNT(*) AS target_count
FROM accounts;

-- VAL-003 orphan account validation
SELECT 'orphan_accounts' AS check_name, COUNT(*) AS failed_rows
FROM accounts a
LEFT JOIN customers c ON a.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- VAL-004 negative balance validation
SELECT 'negative_balances' AS check_name, COUNT(*) AS failed_rows
FROM accounts
WHERE balance_chf < 0;

-- VAL-005 unknown segment validation
SELECT 'unknown_segments' AS check_name, COUNT(*) AS failed_rows
FROM customers
WHERE customer_segment = 'unknown';

-- VAL-006 invalid account type validation
SELECT 'invalid_account_types' AS check_name, COUNT(*) AS failed_rows
FROM accounts
WHERE account_type NOT IN ('current', 'savings', 'other');
