-- Business question: How do scale, value, and outcome rate differ by channel?
-- Expected output: one row per channel, ordered by modeled impact.
SELECT
    channel,
    COUNT(*) AS records,
    COUNT(DISTINCT customer_id) AS entities,
    SUM(annual_spend) AS total_value,
    SUM(order_frequency) AS total_volume,
    SUM(annual_spend * order_frequency) AS modeled_impact,
    AVG(high_value_flag::numeric) AS outcome_rate
FROM project_events
GROUP BY channel
ORDER BY modeled_impact DESC;
