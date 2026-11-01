# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `clause_annotation_id`.

| Field | Type | Definition |
|---|---|---|
| `clause_annotation_id` | string | Unique synthetic record identifier |
| `contract_id` | string | Synthetic entity identifier; can repeat across records |
| `review_date` | date | Synthetic event date |
| `clause_type` | category | Primary clause type dimension |
| `contract_type` | category | Secondary contract type dimension |
| `review_minutes` | number | Continuous exploratory driver with approximately 1% intentional missingness |
| `modeled_review_cost` | number | Positive modeled economic, performance, or operational value |
| `clause_count` | integer | Positive modeled activity or exposure count |
| `qa_issue` | 0/1 | Binary indicator for qa issue |

Missingness is deliberately introduced only in `review_minutes` to support data-quality analysis. No field contains real personal or organizational data.
