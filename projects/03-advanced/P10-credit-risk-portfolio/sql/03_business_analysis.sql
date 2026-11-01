-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        utilization_band,
        risk_band,
        COUNT(*) AS records,
        SUM(balance * days_past_due) AS modeled_impact,
        AVG(defaulted::numeric) AS outcome_rate
    FROM project_events
    GROUP BY utilization_band, risk_band
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY utilization_band ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY utilization_band, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (statement_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (account_id);
