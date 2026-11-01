# P05: Banking Campaign and Customer Behavior

**Level:** Intermediate  
**Industry:** Banking  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A retail bank needs to improve deposit-campaign efficiency by understanding conversion, contact burden, and segment differences without over-targeting vulnerable customers.

**Stakeholders:** Campaign manager, Retail banking, Compliance, Customer experience

## Analytical questions

1. Which segments convert efficiently?
2. Where is contact burden high?
3. Do channel differences persist within segments?

## Hypotheses to investigate

- Digital contacts have lower cost per subscription.
- Repeated contact has diminishing association with conversion.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Contact policy
- Channel mix
- Experiment design

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `deposit_value` across in-scope records |
| Total modeled impact | Sum of `deposit_value × contact_count` |
| Subscription rate | Mean of binary `subscribed` across in-scope records |
| Active entities | Distinct count of `customer_id` |
| Group concentration | Share of total modeled impact by `customer_segment` |

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

The committed data is synthetic, generated with seed `105`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
