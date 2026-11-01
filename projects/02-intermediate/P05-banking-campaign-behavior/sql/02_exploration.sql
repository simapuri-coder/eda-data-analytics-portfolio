-- Business question: How do scale, value, and outcome rate differ by customer segment?
-- Expected output: one row per customer_segment, ordered by modeled impact.
SELECT
    customer_segment,
    COUNT(*) AS records,
    COUNT(DISTINCT customer_id) AS entities,
    SUM(deposit_value) AS total_value,
    SUM(contact_count) AS total_volume,
    SUM(deposit_value * contact_count) AS modeled_impact,
    AVG(subscribed::numeric) AS outcome_rate
FROM project_events
GROUP BY customer_segment
ORDER BY modeled_impact DESC;
