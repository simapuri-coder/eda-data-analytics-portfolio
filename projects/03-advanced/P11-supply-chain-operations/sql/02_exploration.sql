-- Business question: How do scale, value, and outcome rate differ by product family?
-- Expected output: one row per product_family, ordered by modeled impact.
SELECT
    product_family,
    COUNT(*) AS records,
    COUNT(DISTINCT order_id) AS entities,
    SUM(order_profit) AS total_value,
    SUM(units) AS total_volume,
    SUM(order_profit * units) AS modeled_impact,
    AVG(late_delivery::numeric) AS outcome_rate
FROM project_events
GROUP BY product_family
ORDER BY modeled_impact DESC;
