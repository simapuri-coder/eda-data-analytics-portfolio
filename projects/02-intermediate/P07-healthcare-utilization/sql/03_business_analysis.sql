-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        complexity_band,
        service_type,
        COUNT(*) AS records,
        SUM(allowed_charge * service_units) AS modeled_impact,
        AVG(return_visit_30d::numeric) AS outcome_rate
    FROM project_events
    GROUP BY complexity_band, service_type
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY complexity_band ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY complexity_band, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (service_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (beneficiary_id);
