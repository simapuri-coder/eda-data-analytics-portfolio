# Executive Summary: Workforce Demographics and Pay Equity

## Decision context

A workforce strategy team needs weighted descriptive evidence on employment and earnings differences across occupations and demographic groups before commissioning deeper equity analysis.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 517 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 909,239,447.
2. **Highest-impact group.** `Services` contributes the most modeled impact (242,847,106) across 518 records.
3. **Highest outcome rate.** `Services` has the highest employment rate at 80.3%. The portfolio-wide rate is 76.2% (95% Wilson interval 74.5%–77.9%).
4. **Recent movement.** Average modeled impact in the latest three months is +3.1% versus the first three months in the synthetic observation window.

## Observation → evidence → implication → action → validation

- **Observation:** `Services` leads modeled impact. **Evidence:** 242,847,106 impact across 518 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by occupation group. **Evidence:** the top observed group is `Services` at 80.3%, compared with 76.2% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Decompose raw gaps by occupation, geography, and hours before interpretation.
- Publish weighted estimates with uncertainty and minimum sample-size rules.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
