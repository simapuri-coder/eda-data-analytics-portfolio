# Executive Summary: Healthcare Utilization Analytics

## Decision context

A healthcare operations team needs a privacy-safe claims-style analysis of utilization, allowed charges, and service variation to test analytical workflows.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 514 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 10,349,684.
2. **Highest-impact group.** `Specialty` contributes the most modeled impact (2,565,206) across 489 records.
3. **Highest outcome rate.** `Specialty` has the highest 30-day return visit rate at 27.2%. The portfolio-wide rate is 19.5% (95% Wilson interval 17.9%–21.1%).
4. **Recent movement.** Average modeled impact in the latest three months is +33.2% versus the first three months in the synthetic observation window.

## Observation → evidence → implication → action → validation

- **Observation:** `Specialty` leads modeled impact. **Evidence:** 2,565,206 impact across 489 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by service type. **Evidence:** the top observed group is `Specialty` at 27.2%, compared with 19.5% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Use the synthetic results only to validate pipelines and definitions.
- Require clinically reviewed denominators and risk adjustment before operational action.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
