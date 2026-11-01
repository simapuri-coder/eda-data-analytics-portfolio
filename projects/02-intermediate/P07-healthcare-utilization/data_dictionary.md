# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `claim_id`.

| Field | Type | Definition |
|---|---|---|
| `claim_id` | string | Unique synthetic record identifier |
| `beneficiary_id` | string | Synthetic entity identifier; can repeat across records |
| `service_date` | date | Synthetic event date |
| `service_type` | category | Primary service type dimension |
| `complexity_band` | category | Secondary complexity band dimension |
| `length_of_stay` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `allowed_charge` | number | Positive modeled economic, performance, or operational value |
| `service_units` | integer | Positive modeled activity or exposure count |
| `return_visit_30d` | 0/1 | Binary indicator for 30-day return visit |

Missingness is deliberately introduced only in `length_of_stay` to support data-quality analysis. No field contains real personal or organizational data.
