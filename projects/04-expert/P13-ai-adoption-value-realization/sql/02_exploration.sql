-- Business question: How do scale, value, and outcome rate differ by job family?
-- Expected output: one row per job_family, ordered by modeled impact.
SELECT
    job_family,
    COUNT(*) AS records,
    COUNT(DISTINCT respondent_id) AS entities,
    SUM(reported_value_score) AS total_value,
    SUM(tools_used) AS total_volume,
    SUM(reported_value_score * tools_used) AS modeled_impact,
    AVG(frequent_ai_use::numeric) AS outcome_rate
FROM project_events
GROUP BY job_family
ORDER BY modeled_impact DESC;
