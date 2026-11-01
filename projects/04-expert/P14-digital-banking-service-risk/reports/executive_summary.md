# Executive Summary: Digital Banking Service Failure and Retention Risk

## Decision context

A digital banking operations team needs to prioritize complaint themes and response failures while avoiding misleading company rankings without customer denominators.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 517 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 4,707,021.
2. **Highest-impact group.** `Authentication` contributes the most modeled impact (1,164,960) across 514 records.
3. **Highest outcome rate.** `Transfers` has the highest untimely response rate at 29.6%. The portfolio-wide rate is 23.6% (95% Wilson interval 21.9%–25.3%).
4. **Recent movement.** Average modeled impact in the latest three months is -7.1% versus the first three months in the synthetic observation window.

## Observation → evidence → implication → action → validation

- **Observation:** `Authentication` leads modeled impact. **Evidence:** 1,164,960 impact across 514 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by product issue. **Evidence:** the top observed group is `Transfers` at 29.6%, compared with 23.6% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Prioritize theme-level process failures, not raw company rankings.
- Add active-customer denominators before comparing complaint rates across products.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
