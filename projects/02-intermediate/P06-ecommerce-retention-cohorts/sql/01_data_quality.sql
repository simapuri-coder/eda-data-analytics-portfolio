-- Business question: Is the loaded synthetic table complete and structurally usable?
-- Expected output: one row of control counts. Any nonzero duplicate or invalid-outcome count requires investigation.
SELECT
    COUNT(*) AS row_count,
    COUNT(DISTINCT order_id) AS distinct_event_ids,
    COUNT(*) - COUNT(DISTINCT order_id) AS duplicate_event_ids,
    COUNT(*) FILTER (WHERE days_since_prior_order IS NULL) AS missing_driver_values,
    COUNT(*) FILTER (WHERE repeat_order NOT IN (0, 1)) AS invalid_outcomes
FROM project_events;
