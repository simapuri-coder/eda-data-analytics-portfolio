# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `experiment_event_id`.

| Field | Type | Definition |
|---|---|---|
| `experiment_event_id` | string | Unique synthetic record identifier |
| `user_id` | string | Synthetic entity identifier; can repeat across records |
| `assignment_date` | date | Synthetic event date |
| `channel` | category | Primary channel dimension |
| `audience_segment` | category | Secondary audience segment dimension |
| `prior_engagement_score` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `conversion_value` | number | Positive modeled economic, performance, or operational value |
| `impressions` | integer | Positive modeled activity or exposure count |
| `converted` | 0/1 | Binary indicator for conversion |
| `treatment` | 0/1 | Randomized synthetic treatment assignment |

Missingness is deliberately introduced only in `prior_engagement_score` to support data-quality analysis. No field contains real personal or organizational data.
