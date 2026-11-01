-- Business question: How do scale, value, and outcome rate differ by school?
-- Expected output: one row per school, ordered by modeled impact.
SELECT
    school,
    COUNT(*) AS records,
    COUNT(DISTINCT student_id) AS entities,
    SUM(final_grade) AS total_value,
    SUM(absences) AS total_volume,
    SUM(final_grade * absences) AS modeled_impact,
    AVG(passed::numeric) AS outcome_rate
FROM project_events
GROUP BY school
ORDER BY modeled_impact DESC;
