-- Business question: Is the loaded synthetic table complete and structurally usable?
-- Expected output: one row of control counts. Any nonzero duplicate or invalid-outcome count requires investigation.
SELECT
    COUNT(*) AS row_count,
    COUNT(DISTINCT invoice_line_id) AS distinct_event_ids,
    COUNT(*) - COUNT(DISTINCT invoice_line_id) AS duplicate_event_ids,
    COUNT(*) FILTER (WHERE unit_price IS NULL) AS missing_driver_values,
    COUNT(*) FILTER (WHERE cancelled NOT IN (0, 1)) AS invalid_outcomes
FROM project_events;
