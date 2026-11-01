# Executive Summary: Customer Segmentation and Value Tiers

## Decision context

A wholesale distributor needs an exploratory segmentation of customer spending and order intensity to design service hypotheses without assuming clusters are permanent truths.

All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.

## Headline findings

1. **Portfolio scale.** The analysis covers 2,400 records and 517 unique entities from 2024-01-02 through 2025-12-30. Total modeled impact is 1,041,689,666.
2. **Highest-impact group.** `Independent` contributes the most modeled impact (312,597,787) across 602 records.
3. **Highest outcome rate.** `Independent` has the highest high-value flag rate at 34.2%. The portfolio-wide rate is 26.0% (95% Wilson interval 24.3%–27.8%).
4. **Recent movement.** Average modeled impact in the latest three months is -2.3% versus the first three months in the synthetic observation window.
5. **Exploratory segmentation.** A four-cluster solution was produced from standardized value and volume fields. Clusters are descriptive working groups, not natural or permanent customer types.

## Observation → evidence → implication → action → validation

- **Observation:** `Independent` leads modeled impact. **Evidence:** 312,597,787 impact across 602 records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.
- **Observation:** outcome rates vary by channel. **Evidence:** the top observed group is `Independent` at 34.2%, compared with 26.0% overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.

## Recommendations

- Stress-test cluster count and initialization before labeling segments.
- Use clusters to generate service hypotheses, then validate with customer outcomes.

## Limitations

- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.
- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.
- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.
- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.

## Reproducibility

Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.
