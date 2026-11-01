# P01: Retail Sales Performance Analysis

**Level:** Foundational  
**Industry:** Retail  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A retail leadership team needs a consistent view of sales concentration, cancellations, product mix, and market performance before setting inventory and commercial priorities.

**Stakeholders:** Head of Retail, Merchandising, Finance, Operations

## Analytical questions

1. Which categories and markets drive net sales?
2. Where are cancellation rates highest?
3. How concentrated is modeled impact?

## Hypotheses to investigate

- Seasonal merchandise has greater sales volatility.
- Higher-priced lines have different cancellation rates.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Inventory focus
- Category review
- Cancellation root-cause work

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `net_sales` across in-scope records |
| Total modeled impact | Sum of `net_sales × quantity` |
| Cancellation rate | Mean of binary `cancelled` across in-scope records |
| Active entities | Distinct count of `customer_id` |
| Group concentration | Share of total modeled impact by `product_category` |

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

The committed data is synthetic, generated with seed `101`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
