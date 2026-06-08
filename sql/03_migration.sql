INSERT INTO customers (customer_id, customer_segment, country, created_at)
SELECT
    client_ref AS customer_id,
    CASE segment_code
        WHEN 'RET' THEN 'retail'
        WHEN 'PRM' THEN 'premium'
        WHEN 'SME' THEN 'sme'
        ELSE 'unknown'
    END AS customer_segment,
    domicile_country AS country,
    created_date AS created_at
FROM legacy_clients
ON CONFLICT (customer_id) DO NOTHING;

INSERT INTO accounts (account_id, customer_id, account_type, currency, opened_at, balance_chf)
SELECT
    acct_ref AS account_id,
    client_ref AS customer_id,
    CASE acct_type
        WHEN 'CUR' THEN 'current'
        WHEN 'SVG' THEN 'savings'
        ELSE 'other'
    END AS account_type,
    curr AS currency,
    open_date AS opened_at,
    balance_chf
FROM legacy_accounts
ON CONFLICT (account_id) DO NOTHING;
