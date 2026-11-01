# Executive Summary: Product Experimentation and Uplift Analysis

## Decision context

A growth team needs to decide whether a randomized advertising treatment improves conversion enough to justify rollout and which segments require follow-up experiments.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 517 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 986,995.
2. **Highest-impact group.** `Video` contributes the most modeled impact (318,367) across 621 records.
3. **Highest outcome rate.** `Video` has the highest conversion rate at 16.9%. The portfolio-wide rate is 13.7% (95% Wilson interval 12.4%–15.1%).
4. **Recent movement.** Average modeled impact in the latest three months is +6.5% versus the first three months in the synthetic observation window.
5. **Experiment estimate.** Treatment changes the observed outcome rate by +4.29% (95% interval +1.56% to +7.02%, two-sided p=0.002). This estimate is causal only because the synthetic generator randomizes treatment.

## Observation → evidence → implication → action → validation

- **Observation:** `Video` leads modeled impact. **Evidence:** 318,367 impact across 621 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by channel. **Evidence:** the top observed group is `Video` at 16.9%, compared with 13.7% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Base rollout on the pre-specified absolute effect and interval, not p-value alone.
- Treat segment effects as exploratory unless powered and adjusted for multiplicity.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
