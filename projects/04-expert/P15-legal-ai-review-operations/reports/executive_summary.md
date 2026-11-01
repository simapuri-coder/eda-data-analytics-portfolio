# Executive Summary: Legal AI Document Review Operations

## Decision context

A legal AI product team needs to estimate clause-review workload, rare-clause QA coverage, and human capacity without treating automated labels as final legal judgments.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 518 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 1,751,276.
2. **Highest-impact group.** `Assignment` contributes the most modeled impact (425,224) across 462 records.
3. **Highest outcome rate.** `Confidentiality` has the highest qa issue rate at 16.4%. The portfolio-wide rate is 13.0% (95% Wilson interval 11.8%–14.4%).
4. **Recent movement.** Average modeled impact in the latest three months is -10.2% versus the first three months in the synthetic observation window.

## Observation → evidence → implication → action → validation

- **Observation:** `Assignment` leads modeled impact. **Evidence:** 425,224 impact across 462 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by clause type. **Evidence:** the top observed group is `Confidentiality` at 16.4%, compared with 13.0% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Guarantee minimum QA coverage for rare, high-consequence clauses.
- Keep qualified legal review as the final decision point and monitor annotation drift.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
