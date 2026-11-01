-- Business question: How do scale, value, and outcome rate differ by acquisition source?
-- Expected output: one row per acquisition_source, ordered by modeled impact.
SELECT
    acquisition_source,
    COUNT(*) AS records,
    COUNT(DISTINCT customer_id) AS entities,
    SUM(order_value) AS total_value,
    SUM(items) AS total_volume,
    SUM(order_value * items) AS modeled_impact,
    AVG(repeat_order::numeric) AS outcome_rate
FROM project_events
GROUP BY acquisition_source
ORDER BY modeled_impact DESC;
