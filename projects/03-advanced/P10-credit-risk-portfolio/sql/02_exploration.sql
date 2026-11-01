-- Business question: How do scale, value, and outcome rate differ by risk band?
-- Expected output: one row per risk_band, ordered by modeled impact.
SELECT
    risk_band,
    COUNT(*) AS records,
    COUNT(DISTINCT account_id) AS entities,
    SUM(balance) AS total_value,
    SUM(days_past_due) AS total_volume,
    SUM(balance * days_past_due) AS modeled_impact,
    AVG(defaulted::numeric) AS outcome_rate
FROM project_events
GROUP BY risk_band
ORDER BY modeled_impact DESC;
