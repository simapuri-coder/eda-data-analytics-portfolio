# P15: Legal AI Document Review Operations

**Level:** Expert  
**Industry:** Legal technology  
**Data:** deterministic synthetic data generated in this repository

## Business problem

A legal AI product team needs to estimate clause-review workload, rare-clause QA coverage, and human capacity without treating automated labels as final legal judgments.

**Stakeholders:** Legal operations, Product, Machine learning, Quality assurance

## Analytical questions

1. Which clause types drive workload?
2. Where is QA issue prevalence highest?
3. How should rare clauses be sampled?

## Hypotheses to investigate

- Rare clauses require disproportionate QA effort.
- Review time varies by contract type.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- QA sampling
- Human review capacity
- Product prioritization

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `modeled_review_cost` across in-scope records |
| Total modeled impact | Sum of `modeled_review_cost × clause_count` |
| QA issue rate | Mean of binary `qa_issue` across in-scope records |
| Active entities | Distinct count of `contract_id` |
| Group concentration | Share of total modeled impact by `clause_type` |

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

The committed data is synthetic, generated with seed `115`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
