# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `session_id`.

| Field | Type | Definition |
|---|---|---|
| `session_id` | string | Unique synthetic record identifier |
| `visitor_id` | string | Synthetic entity identifier; can repeat across records |
| `session_date` | date | Synthetic event date |
| `deepest_stage` | category | Primary deepest stage dimension |
| `visitor_type` | category | Secondary visitor type dimension |
| `engagement_minutes` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `page_value` | number | Positive modeled economic, performance, or operational value |
| `page_count` | integer | Positive modeled activity or exposure count |
| `purchased` | 0/1 | Binary indicator for purchase |

Missingness is deliberately introduced only in `engagement_minutes` to support data-quality analysis. No field contains real personal or organizational data.
