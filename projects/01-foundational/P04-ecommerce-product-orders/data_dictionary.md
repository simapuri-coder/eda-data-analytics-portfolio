# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `session_event_id`.

| Field | Type | Definition |
|---|---|---|
| `session_event_id` | string | Unique synthetic record identifier |
| `user_id` | string | Synthetic entity identifier; can repeat across records |
| `event_date` | date | Synthetic event date |
| `acquisition_channel` | category | Primary acquisition channel dimension |
| `device` | category | Secondary device dimension |
| `product_views` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `order_value` | number | Positive modeled economic, performance, or operational value |
| `items_viewed` | integer | Positive modeled activity or exposure count |
| `converted` | 0/1 | Binary indicator for conversion |

Missingness is deliberately introduced only in `product_views` to support data-quality analysis. No field contains real personal or organizational data.
