# P10: Credit Risk and Portfolio EDA

**Level:** Advanced  
**Industry:** Consumer credit  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A credit portfolio team needs to explain where delinquency and default risk concentrate before changing policy or building predictive models.

**Stakeholders:** Credit risk, Portfolio management, Fair lending, Finance

## Analytical questions

1. Where do defaults and balances concentrate?
2. Are delinquency patterns monotonic across bands?
3. What features would leak future information?

## Hypotheses to investigate

- Default increases with utilization and delinquency.
- Exposure concentration differs from account-count concentration.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Portfolio monitoring
- Policy investigation
- Feature governance

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `balance` across in-scope records |
| Total modeled impact | Sum of `balance × days_past_due` |
| Default rate | Mean of binary `defaulted` across in-scope records |
| Active entities | Distinct count of `account_id` |
| Group concentration | Share of total modeled impact by `risk_band` |

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

The committed data is synthetic, generated with seed `110`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
