-- Business question: How do scale, value, and outcome rate differ by product issue?
-- Expected output: one row per product_issue, ordered by modeled impact.
SELECT
    product_issue,
    COUNT(*) AS records,
    COUNT(DISTINCT consumer_case_id) AS entities,
    SUM(modeled_retention_value) AS total_value,
    SUM(contacts) AS total_volume,
    SUM(modeled_retention_value * contacts) AS modeled_impact,
    AVG(untimely_response::numeric) AS outcome_rate
FROM project_events
GROUP BY product_issue
ORDER BY modeled_impact DESC;
