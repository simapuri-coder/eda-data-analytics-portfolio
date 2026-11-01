-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        audience_segment,
        channel,
        COUNT(*) AS records,
        SUM(conversion_value * impressions) AS modeled_impact,
        AVG(converted::numeric) AS outcome_rate
    FROM project_events
    GROUP BY audience_segment, channel
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY audience_segment ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY audience_segment, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (assignment_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (user_id);


-- Randomized experiment estimate: absolute difference in conversion rates.
SELECT treatment, COUNT(*) AS n, AVG(converted::numeric) AS outcome_rate
FROM project_events
GROUP BY treatment
ORDER BY treatment;
