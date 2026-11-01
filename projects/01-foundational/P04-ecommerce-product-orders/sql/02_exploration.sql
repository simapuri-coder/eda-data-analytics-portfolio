-- Business question: How do scale, value, and outcome rate differ by acquisition channel?
-- Expected output: one row per acquisition_channel, ordered by modeled impact.
SELECT
    acquisition_channel,
    COUNT(*) AS records,
    COUNT(DISTINCT user_id) AS entities,
    SUM(order_value) AS total_value,
    SUM(items_viewed) AS total_volume,
    SUM(order_value * items_viewed) AS modeled_impact,
    AVG(converted::numeric) AS outcome_rate
FROM project_events
GROUP BY acquisition_channel
ORDER BY modeled_impact DESC;
