-- Business question: How do scale, value, and outcome rate differ by channel?
-- Expected output: one row per channel, ordered by modeled impact.
SELECT
    channel,
    COUNT(*) AS records,
    COUNT(DISTINCT user_id) AS entities,
    SUM(conversion_value) AS total_value,
    SUM(impressions) AS total_volume,
    SUM(conversion_value * impressions) AS modeled_impact,
    AVG(converted::numeric) AS outcome_rate
FROM project_events
GROUP BY channel
ORDER BY modeled_impact DESC;
