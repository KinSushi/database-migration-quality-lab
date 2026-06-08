CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    customer_segment TEXT NOT NULL,
    country TEXT NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS accounts (
    account_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL REFERENCES customers(customer_id),
    account_type TEXT NOT NULL,
    currency TEXT NOT NULL,
    opened_at DATE NOT NULL,
    balance_chf NUMERIC(18, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS validation_results (
    check_id TEXT PRIMARY KEY,
    check_name TEXT NOT NULL,
    status TEXT NOT NULL,
    failed_rows INTEGER NOT NULL,
    executed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reconciliation_results (
    reconciliation_id TEXT PRIMARY KEY,
    reconciliation_name TEXT NOT NULL,
    source_count INTEGER,
    target_count INTEGER,
    count_delta INTEGER,
    source_total NUMERIC(18, 2),
    target_total NUMERIC(18, 2),
    amount_delta NUMERIC(18, 2),
    executed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_accounts_customer_id ON accounts(customer_id);
CREATE INDEX IF NOT EXISTS idx_customers_country ON customers(country);
CREATE INDEX IF NOT EXISTS idx_accounts_currency ON accounts(currency);
