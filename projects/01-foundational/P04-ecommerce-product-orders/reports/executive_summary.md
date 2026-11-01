# Executive Summary: E-commerce Product and Order Analysis

## Decision context

An e-commerce product team needs to understand how acquisition channel, device, and product interactions relate to conversion and revenue.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 514 unique entities from 2024-01-01 through 2025-12-30. Total modeled impact is 2,396,773.
2. **Highest-impact group.** `Referral` contributes the most modeled impact (619,123) across 512 records.
3. **Highest outcome rate.** `Referral` has the highest conversion rate at 26.4%. The portfolio-wide rate is 20.2% (95% Wilson interval 18.6%–21.8%).
4. **Recent movement.** Average modeled impact in the latest three months is +1.0% versus the first three months in the synthetic observation window.

## Observation → evidence → implication → action → validation

- **Observation:** `Referral` leads modeled impact. **Evidence:** 619,123 impact across 512 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by acquisition channel. **Evidence:** the top observed group is `Referral` at 26.4%, compared with 20.2% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Prioritize high-impact channel-device journeys for qualitative review.
- Instrument product-view and checkout events consistently before funnel optimization.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
