# P02: Student Performance and Education Analytics

**Level:** Foundational  
**Industry:** Education  
**Data:** deterministic synthetic data generated in this repository

## Business problem

School leaders need to identify observable performance and attendance patterns so limited support resources can be targeted for further investigation.

**Stakeholders:** Principal, Student support, Teachers, Program evaluator

## Analytical questions

1. How do grades and absences vary by school?
2. What patterns appear across support programs?
3. Which groups need larger samples before action?

## Hypotheses to investigate

- Higher study hours are associated with higher grades.
- Support participation is associated with different pass rates.

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

- Support allocation
- Attendance intervention design
- Measurement improvement

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `final_grade` across in-scope records |
| Total modeled impact | Sum of `final_grade × absences` |
| Pass rate | Mean of binary `passed` across in-scope records |
| Active entities | Distinct count of `student_id` |
| Group concentration | Share of total modeled impact by `school` |

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

The committed data is synthetic, generated with seed `102`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
