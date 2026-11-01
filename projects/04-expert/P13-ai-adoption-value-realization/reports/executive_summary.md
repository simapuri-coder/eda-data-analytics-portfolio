# Executive Summary: AI Tool Adoption and Value Realization

## Decision context

A product and technology leadership team needs to distinguish AI adoption from realized value and identify trust, governance, and cost barriers across user groups.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 512 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 1,138,507.
2. **Highest-impact group.** `Leadership` contributes the most modeled impact (304,902) across 518 records.
3. **Highest outcome rate.** `Leadership` has the highest frequent ai use rate at 61.8%. The portfolio-wide rate is 50.4% (95% Wilson interval 48.4%–52.4%).
4. **Recent movement.** Average modeled impact in the latest three months is +8.3% versus the first three months in the synthetic observation window.

## Observation → evidence → implication → action → validation

- **Observation:** `Leadership` leads modeled impact. **Evidence:** 304,902 impact across 518 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by job family. **Evidence:** the top observed group is `Leadership` at 61.8%, compared with 50.4% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Separate adoption, value, trust, and cost metrics in executive reporting.
- Validate self-reported value with workflow telemetry and pre/post baselines.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
