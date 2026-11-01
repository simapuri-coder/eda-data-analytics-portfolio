# P08: Digital Product Funnel Analysis

**Level:** Intermediate  
**Industry:** Digital commerce  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A digital product team needs to identify where high-value sessions stall and which traffic-device segments deserve instrumentation or experience testing.

**Stakeholders:** Product manager, UX, Growth, Engineering

## Analytical questions

1. Where do sessions stop?
2. Which visitor types have stronger completion?
3. Is engagement associated with value?

## Hypotheses to investigate

- Returning visitors reach deeper stages.
- Longer engagement is associated with purchase.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Funnel instrumentation
- UX experiment priority
- Traffic quality review

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `page_value` across in-scope records |
| Total modeled impact | Sum of `page_value × page_count` |
| Purchase rate | Mean of binary `purchased` across in-scope records |
| Active entities | Distinct count of `visitor_id` |
| Group concentration | Share of total modeled impact by `deepest_stage` |

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

The committed data is synthetic, generated with seed `108`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
