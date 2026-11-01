# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `customer_period_id`.

| Field | Type | Definition |
|---|---|---|
| `customer_period_id` | string | Unique synthetic record identifier |
| `customer_id` | string | Synthetic entity identifier; can repeat across records |
| `period_date` | date | Synthetic event date |
| `channel` | category | Primary channel dimension |
| `region_type` | category | Secondary region type dimension |
| `fresh_share_pct` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `annual_spend` | number | Positive modeled economic, performance, or operational value |
| `order_frequency` | integer | Positive modeled activity or exposure count |
| `high_value_flag` | 0/1 | Binary indicator for high-value flag |

Missingness is deliberately introduced only in `fresh_share_pct` to support data-quality analysis. No field contains real personal or organizational data.
