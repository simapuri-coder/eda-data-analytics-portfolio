-- Business question: How do scale, value, and outcome rate differ by deepest stage?
-- Expected output: one row per deepest_stage, ordered by modeled impact.
SELECT
    deepest_stage,
    COUNT(*) AS records,
    COUNT(DISTINCT visitor_id) AS entities,
    SUM(page_value) AS total_value,
    SUM(page_count) AS total_volume,
    SUM(page_value * page_count) AS modeled_impact,
    AVG(purchased::numeric) AS outcome_rate
FROM project_events
GROUP BY deepest_stage
ORDER BY modeled_impact DESC;
