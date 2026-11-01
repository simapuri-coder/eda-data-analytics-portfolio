-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        region,
        product_family,
        COUNT(*) AS records,
        SUM(order_profit * units) AS modeled_impact,
        AVG(late_delivery::numeric) AS outcome_rate
    FROM project_events
    GROUP BY region, product_family
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY region ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY region, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (ship_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (order_id);
