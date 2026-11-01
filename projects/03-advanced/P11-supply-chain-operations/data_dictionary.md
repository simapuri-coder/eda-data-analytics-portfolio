# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `shipment_line_id`.

| Field | Type | Definition |
|---|---|---|
| `shipment_line_id` | string | Unique synthetic record identifier |
| `order_id` | string | Synthetic entity identifier; can repeat across records |
| `ship_date` | date | Synthetic event date |
| `product_family` | category | Primary product family dimension |
| `region` | category | Secondary region dimension |
| `cycle_time_days` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `order_profit` | number | Positive modeled economic, performance, or operational value |
| `units` | integer | Positive modeled activity or exposure count |
| `late_delivery` | 0/1 | Binary indicator for late delivery |

Missingness is deliberately introduced only in `cycle_time_days` to support data-quality analysis. No field contains real personal or organizational data.
