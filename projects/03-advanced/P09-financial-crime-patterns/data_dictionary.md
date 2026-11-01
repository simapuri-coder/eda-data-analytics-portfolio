# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `transaction_id`.

| Field | Type | Definition |
|---|---|---|
| `transaction_id` | string | Unique synthetic record identifier |
| `account_id` | string | Synthetic entity identifier; can repeat across records |
| `transaction_date` | date | Synthetic event date |
| `payment_type` | category | Primary payment type dimension |
| `account_type` | category | Secondary account type dimension |
| `velocity_score` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `transaction_value` | number | Positive modeled economic, performance, or operational value |
| `transactions_24h` | integer | Positive modeled activity or exposure count |
| `laundering_label` | 0/1 | Binary indicator for laundering label |

Missingness is deliberately introduced only in `velocity_score` to support data-quality analysis. No field contains real personal or organizational data.
