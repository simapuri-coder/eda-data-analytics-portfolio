# Executive Summary: Financial Crime Pattern Exploration

## Decision context

A financial-crime analytics team needs a reproducible synthetic environment to explore transaction velocity, value concentration, and labeled alert patterns without exposing customer data.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 518 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 302,313,402.
2. **Highest-impact group.** `Crypto` contributes the most modeled impact (72,073,798) across 458 records.
3. **Highest outcome rate.** `Crypto` has the highest laundering label rate at 7.4%. The portfolio-wide rate is 5.4% (95% Wilson interval 4.5%–6.4%).
4. **Recent movement.** Average modeled impact in the latest three months is +17.2% versus the first three months in the synthetic observation window.

## Observation → evidence → implication → action → validation

- **Observation:** `Crypto` leads modeled impact. **Evidence:** 72,073,798 impact across 458 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by payment type. **Evidence:** the top observed group is `Crypto` at 7.4%, compared with 5.4% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Optimize for investigator workload and missed-risk tradeoffs, not accuracy alone.
- Review false-alert proxies by account type before threshold changes.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
