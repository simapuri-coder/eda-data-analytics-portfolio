-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        submission_channel,
        product_issue,
        COUNT(*) AS records,
        SUM(modeled_retention_value * contacts) AS modeled_impact,
        AVG(untimely_response::numeric) AS outcome_rate
    FROM project_events
    GROUP BY submission_channel, product_issue
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY submission_channel ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY submission_channel, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (received_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (consumer_case_id);
