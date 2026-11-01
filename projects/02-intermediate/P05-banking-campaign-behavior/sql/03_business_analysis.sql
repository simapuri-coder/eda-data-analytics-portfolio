-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        contact_channel,
        customer_segment,
        COUNT(*) AS records,
        SUM(deposit_value * contact_count) AS modeled_impact,
        AVG(subscribed::numeric) AS outcome_rate
    FROM project_events
    GROUP BY contact_channel, customer_segment
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY contact_channel ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY contact_channel, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (contact_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (customer_id);
