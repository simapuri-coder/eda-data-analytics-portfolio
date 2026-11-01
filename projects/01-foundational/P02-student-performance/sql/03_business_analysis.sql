-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        support_program,
        school,
        COUNT(*) AS records,
        SUM(final_grade * absences) AS modeled_impact,
        AVG(passed::numeric) AS outcome_rate
    FROM project_events
    GROUP BY support_program, school
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY support_program ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY support_program, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events (assessment_date);
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events (student_id);
