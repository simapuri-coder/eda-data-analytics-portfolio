# Executive Summary: Credit Risk and Portfolio EDA

## Decision context

A credit portfolio team needs to explain where delinquency and default risk concentrate before changing policy or building predictive models.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 516 unique entities from 2024-01-01 through 2025-12-29. Total modeled impact is 171,557,450.
2. **Highest-impact group.** `Subprime` contributes the most modeled impact (66,352,316) across 786 records.
3. **Highest outcome rate.** `Subprime` has the highest default rate at 11.8%. The portfolio-wide rate is 10.2% (95% Wilson interval 9.0%–11.4%).
4. **Recent movement.** Average modeled impact in the latest three months is +7.2% versus the first three months in the synthetic observation window.

## Observation → evidence → implication → action → validation

- **Observation:** `Subprime` leads modeled impact. **Evidence:** 66,352,316 impact across 786 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by risk band. **Evidence:** the top observed group is `Subprime` at 11.8%, compared with 10.2% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Separate exposure-weighted and account-weighted risk views.
- Audit temporal leakage before any predictive model or policy simulation.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
