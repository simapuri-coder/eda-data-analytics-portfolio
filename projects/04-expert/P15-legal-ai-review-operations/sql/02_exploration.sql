-- Business question: How do scale, value, and outcome rate differ by clause type?
-- Expected output: one row per clause_type, ordered by modeled impact.
SELECT
    clause_type,
    COUNT(*) AS records,
    COUNT(DISTINCT contract_id) AS entities,
    SUM(modeled_review_cost) AS total_value,
    SUM(clause_count) AS total_volume,
    SUM(modeled_review_cost * clause_count) AS modeled_impact,
    AVG(qa_issue::numeric) AS outcome_rate
FROM project_events
GROUP BY clause_type
ORDER BY modeled_impact DESC;
