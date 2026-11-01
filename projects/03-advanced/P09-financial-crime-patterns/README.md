# P09: Financial Crime Pattern Exploration

**Level:** Advanced  
**Industry:** Financial services  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A financial-crime analytics team needs a reproducible synthetic environment to explore transaction velocity, value concentration, and labeled alert patterns without exposing customer data.

**Stakeholders:** AML investigators, Model risk, Compliance, Data engineering

## Analytical questions

1. Which patterns concentrate labeled alerts?
2. How heavy-tailed are transaction values?
3. Which rules could create excess alerts?

## Hypotheses to investigate

- High velocity is associated with alert labels.
- A small number of payment types drive modeled exposure.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Investigator queue design
- Rule review
- Data-quality controls

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `transaction_value` across in-scope records |
| Total modeled impact | Sum of `transaction_value × transactions_24h` |
| Laundering label rate | Mean of binary `laundering_label` across in-scope records |
| Active entities | Distinct count of `account_id` |
| Group concentration | Share of total modeled impact by `payment_type` |

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

The committed data is synthetic, generated with seed `109`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
