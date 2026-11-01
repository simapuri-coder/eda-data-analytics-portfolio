-- Business question: Is the loaded synthetic table complete and structurally usable?
-- Expected output: one row of control counts. Any nonzero duplicate or invalid-outcome count requires investigation.
SELECT
    COUNT(*) AS row_count,
    COUNT(DISTINCT contact_id) AS distinct_event_ids,
    COUNT(*) - COUNT(DISTINCT contact_id) AS duplicate_event_ids,
    COUNT(*) FILTER (WHERE contact_duration IS NULL) AS missing_driver_values,
    COUNT(*) FILTER (WHERE subscribed NOT IN (0, 1)) AS invalid_outcomes
FROM project_events;
