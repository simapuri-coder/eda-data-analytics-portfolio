# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `assessment_id`.

| Field | Type | Definition |
|---|---|---|
| `assessment_id` | string | Unique synthetic record identifier |
| `student_id` | string | Synthetic entity identifier; can repeat across records |
| `assessment_date` | date | Synthetic event date |
| `school` | category | Primary school dimension |
| `support_program` | category | Secondary support program dimension |
| `study_hours` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `final_grade` | number | Positive modeled economic, performance, or operational value |
| `absences` | integer | Positive modeled activity or exposure count |
| `passed` | 0/1 | Binary indicator for pass |

Missingness is deliberately introduced only in `study_hours` to support data-quality analysis. No field contains real personal or organizational data.
