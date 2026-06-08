-- Row counts
SELECT 'legacy_clients' AS table_name, COUNT(*) AS row_count FROM legacy_clients
UNION ALL SELECT 'legacy_accounts', COUNT(*) FROM legacy_accounts
UNION ALL SELECT 'customers', COUNT(*) FROM customers
UNION ALL SELECT 'accounts', COUNT(*) FROM accounts;

-- EXPLAIN validation path
EXPLAIN
SELECT a.*
FROM accounts a
LEFT JOIN customers c ON a.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- Future notes:
-- For large migrations, validate batch sizes, add staging tables and review indexes
-- on natural keys, foreign keys and business-critical reconciliation fields.
