-- Business question: Is the loaded synthetic table complete and structurally usable?
-- Expected output: one row of control counts. Any nonzero duplicate or invalid-outcome count requires investigation.
SELECT
    COUNT(*) AS row_count,
    COUNT(DISTINCT customer_period_id) AS distinct_event_ids,
    COUNT(*) - COUNT(DISTINCT customer_period_id) AS duplicate_event_ids,
    COUNT(*) FILTER (WHERE fresh_share_pct IS NULL) AS missing_driver_values,
    COUNT(*) FILTER (WHERE high_value_flag NOT IN (0, 1)) AS invalid_outcomes
FROM project_events;
