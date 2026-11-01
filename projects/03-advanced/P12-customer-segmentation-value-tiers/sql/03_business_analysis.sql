-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        region_type,
        channel,
        COUNT(*) AS records,
        SUM(annual_spend * order_frequency) AS modeled_impact,
        AVG(high_value_flag::numeric) AS outcome_rate
    FROM project_events
    GROUP BY region_type, channel
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY region_type ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY region_type, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (period_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (customer_id);
