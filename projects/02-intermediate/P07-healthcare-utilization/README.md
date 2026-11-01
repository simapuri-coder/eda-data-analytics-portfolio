# P07: Healthcare Utilization Analytics

**Level:** Intermediate  
**Industry:** Healthcare  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A healthcare operations team needs a privacy-safe claims-style analysis of utilization, allowed charges, and service variation to test analytical workflows.

**Stakeholders:** Healthcare operations, Clinical finance, Data governance, Care management

## Analytical questions

1. Which service types drive utilization and charges?
2. Where do return-visit patterns differ?
3. Which findings are invalid for real beneficiaries?

## Hypotheses to investigate

- Higher complexity is associated with higher allowed charges.
- Return-visit rates vary by service type.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Analytical workflow design
- Care-review prioritization
- Data acquisition

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `allowed_charge` across in-scope records |
| Total modeled impact | Sum of `allowed_charge × service_units` |
| 30-day return visit rate | Mean of binary `return_visit_30d` across in-scope records |
| Active entities | Distinct count of `beneficiary_id` |
| Group concentration | Share of total modeled impact by `service_type` |

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

The committed data is synthetic, generated with seed `107`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
