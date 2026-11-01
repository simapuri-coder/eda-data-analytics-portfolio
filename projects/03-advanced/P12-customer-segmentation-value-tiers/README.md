# P12: Customer Segmentation and Value Tiers

**Level:** Advanced  
**Industry:** Wholesale distribution  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A wholesale distributor needs an exploratory segmentation of customer spending and order intensity to design service hypotheses without assuming clusters are permanent truths.

**Stakeholders:** Commercial strategy, Account management, Finance, Customer operations

## Analytical questions

1. Which spending and frequency profiles emerge?
2. Are clusters stable?
3. How should service hypotheses differ by profile?

## Hypotheses to investigate

- Spending and order frequency form distinct profiles.
- Channel mix explains part of segment differences.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Service design
- Account coverage
- Segmentation research

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `annual_spend` across in-scope records |
| Total modeled impact | Sum of `annual_spend × order_frequency` |
| High-value flag rate | Mean of binary `high_value_flag` across in-scope records |
| Active entities | Distinct count of `customer_id` |
| Group concentration | Share of total modeled impact by `channel` |

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

The committed data is synthetic, generated with seed `112`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
