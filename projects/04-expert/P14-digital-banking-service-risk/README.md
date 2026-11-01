# P14: Digital Banking Service Failure and Retention Risk

**Level:** Expert  
**Industry:** Consumer banking  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A digital banking operations team needs to prioritize complaint themes and response failures while avoiding misleading company rankings without customer denominators.

**Stakeholders:** Digital banking, Complaint operations, Compliance, Customer experience

## Analytical questions

1. Which themes are growing?
2. Where are responses slow?
3. What conclusions require market-share denominators?

## Hypotheses to investigate

- Authentication complaints have different response times.
- Repeated contacts are associated with untimely response.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Operational investigation
- Issue taxonomy
- Response SLA

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `modeled_retention_value` across in-scope records |
| Total modeled impact | Sum of `modeled_retention_value × contacts` |
| Untimely response rate | Mean of binary `untimely_response` across in-scope records |
| Active entities | Distinct count of `consumer_case_id` |
| Group concentration | Share of total modeled impact by `product_issue` |

## Repository contents

- `data/raw/synthetic_data.csv` — generated input with no real people or organizations
- `data/processed/` — calculated QA, KPI, trend, and method-specific outputs
- `src/generate_data.py` — reproducible data generator entry point
- `src/analysis.py` — full analysis entry point
- `sql/` — PostgreSQL quality, exploration, and business queries
- `notebooks/eda_analysis.ipynb` — narrative runnable notebook
- `visualizations/` — generated SVG charts
- `reports/executive_summary.md` — evidence-backed decision summary
- `data_dictionary.md` — field definitions and grain

## Run locally

From this project directory:

```bash
python src/generate_data.py
python src/analysis.py
```

Or run the full portfolio from the repository root:

```bash
python run_all.py
python -m unittest discover -s tests
```

## Integrity statement

The committed data is synthetic, generated with seed `114`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
