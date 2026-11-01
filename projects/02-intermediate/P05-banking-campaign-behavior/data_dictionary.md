# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `contact_id`.

| Field | Type | Definition |
|---|---|---|
| `contact_id` | string | Unique synthetic record identifier |
| `customer_id` | string | Synthetic entity identifier; can repeat across records |
| `contact_date` | date | Synthetic event date |
| `customer_segment` | category | Primary customer segment dimension |
| `contact_channel` | category | Secondary contact channel dimension |
| `contact_duration` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `deposit_value` | number | Positive modeled economic, performance, or operational value |
| `contact_count` | integer | Positive modeled activity or exposure count |
| `subscribed` | 0/1 | Binary indicator for subscription |

Missingness is deliberately introduced only in `contact_duration` to support data-quality analysis. No field contains real personal or organizational data.
