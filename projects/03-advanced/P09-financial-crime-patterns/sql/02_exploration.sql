-- Business question: How do scale, value, and outcome rate differ by payment type?
-- Expected output: one row per payment_type, ordered by modeled impact.
SELECT
    payment_type,
    COUNT(*) AS records,
    COUNT(DISTINCT account_id) AS entities,
    SUM(transaction_value) AS total_value,
    SUM(transactions_24h) AS total_volume,
    SUM(transaction_value * transactions_24h) AS modeled_impact,
    AVG(laundering_label::numeric) AS outcome_rate
FROM project_events
GROUP BY payment_type
ORDER BY modeled_impact DESC;
