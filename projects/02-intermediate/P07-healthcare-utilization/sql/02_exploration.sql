-- Business question: How do scale, value, and outcome rate differ by service type?
-- Expected output: one row per service_type, ordered by modeled impact.
SELECT
    service_type,
    COUNT(*) AS records,
    COUNT(DISTINCT beneficiary_id) AS entities,
    SUM(allowed_charge) AS total_value,
    SUM(service_units) AS total_volume,
    SUM(allowed_charge * service_units) AS modeled_impact,
    AVG(return_visit_30d::numeric) AS outcome_rate
FROM project_events
GROUP BY service_type
ORDER BY modeled_impact DESC;
