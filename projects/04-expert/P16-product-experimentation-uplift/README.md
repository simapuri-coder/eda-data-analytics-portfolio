# P16: Product Experimentation and Uplift Analysis

**Level:** Expert  
**Industry:** Advertising technology  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A growth team needs to decide whether a randomized advertising treatment improves conversion enough to justify rollout and which segments require follow-up experiments.

**Stakeholders:** Growth product, Marketing science, Finance, Experimentation platform

## Analytical questions

1. Is assignment balanced?
2. What is the absolute treatment effect?
3. Does practical value justify rollout?

## Hypotheses to investigate

- Treatment increases conversion.
- Effect size differs by pre-specified audience segment.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Rollout
- Experiment iteration
- Budget allocation

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `conversion_value` across in-scope records |
| Total modeled impact | Sum of `conversion_value × impressions` |
| Conversion rate | Mean of binary `converted` across in-scope records |
| Active entities | Distinct count of `user_id` |
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

The committed data is synthetic, generated with seed `116`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
