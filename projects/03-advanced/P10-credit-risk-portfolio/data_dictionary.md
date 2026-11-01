# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `account_month_id`.

| Field | Type | Definition |
|---|---|---|
| `account_month_id` | string | Unique synthetic record identifier |
| `account_id` | string | Synthetic entity identifier; can repeat across records |
| `statement_date` | date | Synthetic event date |
| `risk_band` | category | Primary risk band dimension |
| `utilization_band` | category | Secondary utilization band dimension |
| `utilization_pct` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `balance` | number | Positive modeled economic, performance, or operational value |
| `days_past_due` | integer | Positive modeled activity or exposure count |
| `defaulted` | 0/1 | Binary indicator for default |

Missingness is deliberately introduced only in `utilization_pct` to support data-quality analysis. No field contains real personal or organizational data.
