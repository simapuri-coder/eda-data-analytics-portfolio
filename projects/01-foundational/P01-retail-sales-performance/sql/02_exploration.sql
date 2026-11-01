-- Business question: How do scale, value, and outcome rate differ by product category?
-- Expected output: one row per product_category, ordered by modeled impact.
SELECT
    product_category,
    COUNT(*) AS records,
    COUNT(DISTINCT customer_id) AS entities,
    SUM(net_sales) AS total_value,
    SUM(quantity) AS total_volume,
    SUM(net_sales * quantity) AS modeled_impact,
    AVG(cancelled::numeric) AS outcome_rate
FROM project_events
GROUP BY product_category
ORDER BY modeled_impact DESC;
