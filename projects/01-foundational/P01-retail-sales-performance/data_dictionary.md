# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `invoice_line_id`.

| Field | Type | Definition |
|---|---|---|
| `invoice_line_id` | string | Unique synthetic record identifier |
| `customer_id` | string | Synthetic entity identifier; can repeat across records |
| `invoice_date` | date | Synthetic event date |
| `product_category` | category | Primary product category dimension |
| `market` | category | Secondary market dimension |
| `unit_price` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `net_sales` | number | Positive modeled economic, performance, or operational value |
| `quantity` | integer | Positive modeled activity or exposure count |
| `cancelled` | 0/1 | Binary indicator for cancellation |

Missingness is deliberately introduced only in `unit_price` to support data-quality analysis. No field contains real personal or organizational data.
