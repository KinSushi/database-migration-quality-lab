CREATE TABLE IF NOT EXISTS legacy_clients (
    client_ref TEXT PRIMARY KEY,
    segment_code TEXT NOT NULL,
    domicile_country TEXT NOT NULL,
    created_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS legacy_accounts (
    acct_ref TEXT PRIMARY KEY,
    client_ref TEXT NOT NULL,
    acct_type TEXT NOT NULL,
    curr TEXT NOT NULL,
    open_date DATE NOT NULL,
    balance_chf NUMERIC(18, 2) NOT NULL
);
