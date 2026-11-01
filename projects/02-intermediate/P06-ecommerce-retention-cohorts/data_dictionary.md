# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `order_id`.

| Field | Type | Definition |
|---|---|---|
| `order_id` | string | Unique synthetic record identifier |
| `customer_id` | string | Synthetic entity identifier; can repeat across records |
| `order_date` | date | Synthetic event date |
| `acquisition_source` | category | Primary acquisition source dimension |
| `customer_state` | category | Secondary customer state dimension |
| `days_since_prior_order` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `order_value` | number | Positive modeled economic, performance, or operational value |
| `items` | integer | Positive modeled activity or exposure count |
| `repeat_order` | 0/1 | Binary indicator for repeat order |

Missingness is deliberately introduced only in `days_since_prior_order` to support data-quality analysis. No field contains real personal or organizational data.
