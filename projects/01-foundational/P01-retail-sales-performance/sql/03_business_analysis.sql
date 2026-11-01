-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        market,
        product_category,
        COUNT(*) AS records,
        SUM(net_sales * quantity) AS modeled_impact,
        AVG(cancelled::numeric) AS outcome_rate
    FROM project_events
    GROUP BY market, product_category
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY market ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY market, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (invoice_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (customer_id);
