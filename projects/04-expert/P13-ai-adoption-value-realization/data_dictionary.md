# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `survey_response_id`.

| Field | Type | Definition |
|---|---|---|
| `survey_response_id` | string | Unique synthetic record identifier |
| `respondent_id` | string | Synthetic entity identifier; can repeat across records |
| `response_date` | date | Synthetic event date |
| `job_family` | category | Primary job family dimension |
| `role_level` | category | Secondary role level dimension |
| `weekly_ai_hours` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `reported_value_score` | number | Positive modeled economic, performance, or operational value |
| `tools_used` | integer | Positive modeled activity or exposure count |
| `frequent_ai_use` | 0/1 | Binary indicator for frequent ai use |

Missingness is deliberately introduced only in `weekly_ai_hours` to support data-quality analysis. No field contains real personal or organizational data.
