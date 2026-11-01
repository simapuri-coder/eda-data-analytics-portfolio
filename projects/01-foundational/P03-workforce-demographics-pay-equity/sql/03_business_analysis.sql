-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        demographic_group,
        occupation_group,
        COUNT(*) AS records,
        SUM(annual_earnings * person_weight) AS modeled_impact,
        AVG(employed::numeric) AS outcome_rate
    FROM project_events
    GROUP BY demographic_group, occupation_group
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY demographic_group ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY demographic_group, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (survey_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (worker_id);
