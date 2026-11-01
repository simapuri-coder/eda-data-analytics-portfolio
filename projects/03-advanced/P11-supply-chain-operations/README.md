# P11: Supply Chain Operations Analytics

**Level:** Advanced  
**Industry:** Supply chain  
**Data:** deterministic synthetic data generated in this repository

## Business problem

An operations leader needs to prioritize the product-region combinations responsible for late delivery, long cycle time, and modeled margin exposure.

**Stakeholders:** Supply chain VP, Fulfillment, Procurement, Finance

## Analytical questions

1. Where are delays and profit concentrated?
2. Which groups show unstable cycle time?
3. What process areas deserve root-cause analysis?

## Hypotheses to investigate

- Cycle time is associated with late delivery.
- Profit and service risk concentrate in different groups.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Root-cause priority
- SLA review
- Capacity planning

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `order_profit` across in-scope records |
| Total modeled impact | Sum of `order_profit × units` |
| Late delivery rate | Mean of binary `late_delivery` across in-scope records |
| Active entities | Distinct count of `order_id` |
| Group concentration | Share of total modeled impact by `product_family` |

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

The committed data is synthetic, generated with seed `111`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
