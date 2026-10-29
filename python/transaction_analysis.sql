
-- Telangana Rice Mill Transaction Analytics
-- PostgreSQL analysis examples

-- 1. View the first 10 records
SELECT *
FROM rice_mill_transactions
LIMIT 10;

-- 2. Count the total number of records
SELECT COUNT(*) AS total_transactions
FROM rice_mill_transactions;

-- 3. Check for missing values in a selected column
-- Replace transaction_id with the actual column name
-- if your dataset uses a different name.
SELECT COUNT(*) AS missing_transaction_ids
FROM rice_mill_transactions
WHERE transaction_id IS NULL;
