# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `survey_record_id`.

| Field | Type | Definition |
|---|---|---|
| `survey_record_id` | string | Unique synthetic record identifier |
| `worker_id` | string | Synthetic entity identifier; can repeat across records |
| `survey_date` | date | Synthetic event date |
| `occupation_group` | category | Primary occupation group dimension |
| `demographic_group` | category | Secondary demographic group dimension |
| `hours_per_week` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `annual_earnings` | number | Positive modeled economic, performance, or operational value |
| `person_weight` | integer | Positive modeled activity or exposure count |
| `employed` | 0/1 | Binary indicator for employment |

Missingness is deliberately introduced only in `hours_per_week` to support data-quality analysis. No field contains real personal or organizational data.
