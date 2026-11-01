-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        role_level,
        job_family,
        COUNT(*) AS records,
        SUM(reported_value_score * tools_used) AS modeled_impact,
        AVG(frequent_ai_use::numeric) AS outcome_rate
    FROM project_events
    GROUP BY role_level, job_family
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY role_level ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY role_level, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (response_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (respondent_id);
