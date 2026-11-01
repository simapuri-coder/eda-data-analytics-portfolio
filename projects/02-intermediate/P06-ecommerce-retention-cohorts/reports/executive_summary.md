# Executive Summary: E-commerce Retention and Cohort Analysis

## Decision context

A lifecycle team needs cohort evidence on repeat purchase and customer value to prioritize onboarding and retention experiments.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 519 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 1,294,057.
2. **Highest-impact group.** `Email` contributes the most modeled impact (379,337) across 588 records.
3. **Highest outcome rate.** `Email` has the highest repeat order rate at 41.0%. The portfolio-wide rate is 32.5% (95% Wilson interval 30.7%–34.4%).
4. **Recent movement.** Average modeled impact in the latest three months is +15.9% versus the first three months in the synthetic observation window.
5. **Cohort coverage.** The retention output spans 22 acquisition cohorts. Later cohorts have shorter observable follow-up and should not be compared at unavailable ages.

## Observation → evidence → implication → action → validation

- **Observation:** `Email` leads modeled impact. **Evidence:** 379,337 impact across 588 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by acquisition source. **Evidence:** the top observed group is `Email` at 41.0%, compared with 32.5% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Compare cohorts only at equal observable ages.
- Test onboarding interventions within acquisition source to reduce mix bias.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
