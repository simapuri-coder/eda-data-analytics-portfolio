-- Business question: How do scale, value, and outcome rate differ by occupation group?
-- Expected output: one row per occupation_group, ordered by modeled impact.
SELECT
    occupation_group,
    COUNT(*) AS records,
    COUNT(DISTINCT worker_id) AS entities,
    SUM(annual_earnings) AS total_value,
    SUM(person_weight) AS total_volume,
    SUM(annual_earnings * person_weight) AS modeled_impact,
    AVG(employed::numeric) AS outcome_rate
FROM project_events
GROUP BY occupation_group
ORDER BY modeled_impact DESC;
