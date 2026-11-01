-- Business question: Is the loaded synthetic table complete and structurally usable?
-- Expected output: one row of control counts. Any nonzero duplicate or invalid-outcome count requires investigation.
SELECT
    COUNT(*) AS row_count,
    COUNT(DISTINCT experiment_event_id) AS distinct_event_ids,
    COUNT(*) - COUNT(DISTINCT experiment_event_id) AS duplicate_event_ids,
    COUNT(*) FILTER (WHERE prior_engagement_score IS NULL) AS missing_driver_values,
    COUNT(*) FILTER (WHERE converted NOT IN (0, 1)) AS invalid_outcomes
FROM project_events;
