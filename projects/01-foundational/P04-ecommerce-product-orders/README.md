# P04: E-commerce Product and Order Analysis

**Level:** Foundational  
**Industry:** E-commerce  
**Data:** deterministic synthetic data generated in this repository

## Business problem

An e-commerce product team needs to understand how acquisition channel, device, and product interactions relate to conversion and revenue.

**Stakeholders:** Product manager, Growth, Merchandising, Analytics engineering

## Analytical questions

1. Which channel-device combinations have strong conversion?
2. How does product depth relate to order value?
3. Where does revenue concentration create risk?

## Hypotheses to investigate

- Returning direct traffic converts at a higher rate.
- Sessions with more product views have higher order value.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Channel investment
- Device experience prioritization
- Merchandising

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `order_value` across in-scope records |
| Total modeled impact | Sum of `order_value × items_viewed` |
| Conversion rate | Mean of binary `converted` across in-scope records |
| Active entities | Distinct count of `user_id` |
| Group concentration | Share of total modeled impact by `acquisition_channel` |

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

The committed data is synthetic, generated with seed `104`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
