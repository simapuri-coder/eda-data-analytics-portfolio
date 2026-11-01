# P13: AI Tool Adoption and Value Realization

**Level:** Expert  
**Industry:** Technology  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A product and technology leadership team needs to distinguish AI adoption from realized value and identify trust, governance, and cost barriers across user groups.

**Stakeholders:** AI product leader, Engineering leadership, Finance, Risk and compliance

## Analytical questions

1. Who adopts AI tools frequently?
2. Where is value reported?
3. Which barriers require product versus governance action?

## Hypotheses to investigate

- Adoption and reported value differ by role.
- High use does not always imply trust or value.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Enablement investment
- Product roadmap
- Governance

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `reported_value_score` across in-scope records |
| Total modeled impact | Sum of `reported_value_score × tools_used` |
| Frequent AI use rate | Mean of binary `frequent_ai_use` across in-scope records |
| Active entities | Distinct count of `respondent_id` |
| Group concentration | Share of total modeled impact by `job_family` |

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

The committed data is synthetic, generated with seed `113`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
