# P06: E-commerce Retention and Cohort Analysis

**Level:** Intermediate  
**Industry:** E-commerce  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A lifecycle team needs cohort evidence on repeat purchase and customer value to prioritize onboarding and retention experiments.

**Stakeholders:** Lifecycle marketing, Product, Finance, Customer success

## Analytical questions

1. Which acquisition cohorts retain?
2. How does repeat value evolve?
3. How does censoring affect recent cohorts?

## Hypotheses to investigate

- Organic cohorts retain longer.
- Shorter time to second order is associated with stronger later value.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Onboarding investment
- Retention experiment targets
- Cohort monitoring

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `order_value` across in-scope records |
| Total modeled impact | Sum of `order_value × items` |
| Repeat order rate | Mean of binary `repeat_order` across in-scope records |
| Active entities | Distinct count of `customer_id` |
| Group concentration | Share of total modeled impact by `acquisition_source` |

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

The committed data is synthetic, generated with seed `106`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
