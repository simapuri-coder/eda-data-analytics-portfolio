# P03: Workforce Demographics and Pay Equity

**Level:** Foundational  
**Industry:** Labor economics  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A workforce strategy team needs weighted descriptive evidence on employment and earnings differences across occupations and demographic groups before commissioning deeper equity analysis.

**Stakeholders:** Workforce strategy, Policy analysts, HR analytics, Community partners

## Analytical questions

1. Which occupation groups have the highest weighted earnings?
2. How does employment vary across demographic groups?
3. Where are sample-size limits material?

## Hypotheses to investigate

- Earnings differ by occupation mix.
- Raw group gaps narrow after stratifying by occupation.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Research prioritization
- Program targeting
- Data collection

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `annual_earnings` across in-scope records |
| Total modeled impact | Sum of `annual_earnings × person_weight` |
| Employment rate | Mean of binary `employed` across in-scope records |
| Active entities | Distinct count of `worker_id` |
| Group concentration | Share of total modeled impact by `occupation_group` |

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

The committed data is synthetic, generated with seed `103`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
