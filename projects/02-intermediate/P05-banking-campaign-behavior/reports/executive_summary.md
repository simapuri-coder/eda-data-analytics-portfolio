# Executive Summary: Banking Campaign and Customer Behavior

## Decision context

A retail bank needs to improve deposit-campaign efficiency by understanding conversion, contact burden, and segment differences without over-targeting vulnerable customers.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 516 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 27,974,709.
2. **Highest-impact group.** `Youth` contributes the most modeled impact (8,207,123) across 601 records.
3. **Highest outcome rate.** `Youth` has the highest subscription rate at 26.3%. The portfolio-wide rate is 20.1% (95% Wilson interval 18.5%–21.7%).
4. **Recent movement.** Average modeled impact in the latest three months is -13.9% versus the first three months in the synthetic observation window.

## Observation → evidence → implication → action → validation

- **Observation:** `Youth` leads modeled impact. **Evidence:** 8,207,123 impact across 601 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by customer segment. **Evidence:** the top observed group is `Youth` at 26.3%, compared with 20.1% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Set contact-frequency guardrails and track opt-outs.
- Randomize eligible customers across channels before claiming channel effects.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
