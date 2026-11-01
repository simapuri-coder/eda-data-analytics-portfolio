# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `complaint_id`.

| Field | Type | Definition |
|---|---|---|
| `complaint_id` | string | Unique synthetic record identifier |
| `consumer_case_id` | string | Synthetic entity identifier; can repeat across records |
| `received_date` | date | Synthetic event date |
| `product_issue` | category | Primary product issue dimension |
| `submission_channel` | category | Secondary submission channel dimension |
| `response_days` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `modeled_retention_value` | number | Positive modeled economic, performance, or operational value |
| `contacts` | integer | Positive modeled activity or exposure count |
| `untimely_response` | 0/1 | Binary indicator for untimely response |

Missingness is deliberately introduced only in `response_days` to support data-quality analysis. No field contains real personal or organizational data.
