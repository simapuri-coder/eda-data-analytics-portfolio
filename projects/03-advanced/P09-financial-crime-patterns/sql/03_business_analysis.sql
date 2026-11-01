-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        account_type,
        payment_type,
        COUNT(*) AS records,
        SUM(transaction_value * transactions_24h) AS modeled_impact,
        AVG(laundering_label::numeric) AS outcome_rate
    FROM project_events
    GROUP BY account_type, payment_type
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY account_type ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY account_type, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (transaction_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (account_id);
