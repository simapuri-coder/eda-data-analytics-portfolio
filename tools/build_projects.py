"""Build all 16 portfolio projects from explicit project specifications."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from portfolio_core import run_project, write_manifest  # noqa: E402


LEVEL_DIRS = {
    "Foundational": "01-foundational",
    "Intermediate": "02-intermediate",
    "Advanced": "03-advanced",
    "Expert": "04-expert",
}


def schema(event, entity, date, group, group_label, segment, segment_label, driver, value, volume, outcome, outcome_label, treatment=None):
    result = {
        "event_id_col": event,
        "entity_id_col": entity,
        "date_col": date,
        "group_col": group,
        "group_label": group_label,
        "segment_col": segment,
        "segment_label": segment_label,
        "driver_col": driver,
        "value_col": value,
        "volume_col": volume,
        "outcome_col": outcome,
        "outcome_label": outcome_label,
    }
    if treatment:
        result["treatment_col"] = treatment
    return result


PROJECTS = [
    dict(id="P01", level="Foundational", slug="retail-sales-performance", title="Retail Sales Performance Analysis", industry="Retail", seed=101,
         problem_statement="A retail leadership team needs a consistent view of sales concentration, cancellations, product mix, and market performance before setting inventory and commercial priorities.",
         stakeholders=["Head of Retail", "Merchandising", "Finance", "Operations"], groups=["Home", "Gifts", "Office", "Seasonal"], segments=["UK", "EU", "North America", "Other"],
         schema=schema("invoice_line_id", "customer_id", "invoice_date", "product_category", "Product category", "market", "Market", "unit_price", "net_sales", "quantity", "cancelled", "Cancellation"),
         questions=["Which categories and markets drive net sales?", "Where are cancellation rates highest?", "How concentrated is modeled impact?"],
         hypotheses=["Seasonal merchandise has greater sales volatility.", "Higher-priced lines have different cancellation rates."],
         decisions=["Inventory focus", "Category review", "Cancellation root-cause work"],
         recommendations=["Investigate the highest-impact category's availability and cancellation drivers.", "Create a monthly exception review for categories with both high impact and above-average cancellations."], value_mean=85, volume_mean=4),
    dict(id="P02", level="Foundational", slug="student-performance", title="Student Performance and Education Analytics", industry="Education", seed=102,
         problem_statement="School leaders need to identify observable performance and attendance patterns so limited support resources can be targeted for further investigation.",
         stakeholders=["Principal", "Student support", "Teachers", "Program evaluator"], groups=["School A", "School B", "School C"], segments=["No support", "Academic support", "Family support", "Both supports"],
         schema=schema("assessment_id", "student_id", "assessment_date", "school", "School", "support_program", "Support program", "study_hours", "final_grade", "absences", "passed", "Pass"),
         questions=["How do grades and absences vary by school?", "What patterns appear across support programs?", "Which groups need larger samples before action?"],
         hypotheses=["Higher study hours are associated with higher grades.", "Support participation is associated with different pass rates."], decisions=["Support allocation", "Attendance intervention design", "Measurement improvement"],
         recommendations=["Target diagnostic interviews where absence and pass patterns diverge.", "Evaluate support programs prospectively rather than treating observed associations as program effects."], value_mean=72, volume_mean=6, outcome_intercept=0.2),
    dict(id="P03", level="Foundational", slug="workforce-demographics-pay-equity", title="Workforce Demographics and Pay Equity", industry="Labor economics", seed=103,
         problem_statement="A workforce strategy team needs weighted descriptive evidence on employment and earnings differences across occupations and demographic groups before commissioning deeper equity analysis.",
         stakeholders=["Workforce strategy", "Policy analysts", "HR analytics", "Community partners"], groups=["Technology", "Healthcare", "Operations", "Education", "Services"], segments=["Group A", "Group B", "Group C", "Group D"],
         schema=schema("survey_record_id", "worker_id", "survey_date", "occupation_group", "Occupation group", "demographic_group", "Demographic group", "hours_per_week", "annual_earnings", "person_weight", "employed", "Employment"),
         questions=["Which occupation groups have the highest weighted earnings?", "How does employment vary across demographic groups?", "Where are sample-size limits material?"],
         hypotheses=["Earnings differ by occupation mix.", "Raw group gaps narrow after stratifying by occupation."], decisions=["Research prioritization", "Program targeting", "Data collection"],
         recommendations=["Decompose raw gaps by occupation, geography, and hours before interpretation.", "Publish weighted estimates with uncertainty and minimum sample-size rules."], value_mean=62000, value_sigma=0.35, volume_mean=3, driver_mean=39, driver_sd=8, outcome_intercept=1.2),
    dict(id="P04", level="Foundational", slug="ecommerce-product-orders", title="E-commerce Product and Order Analysis", industry="E-commerce", seed=104,
         problem_statement="An e-commerce product team needs to understand how acquisition channel, device, and product interactions relate to conversion and revenue.",
         stakeholders=["Product manager", "Growth", "Merchandising", "Analytics engineering"], groups=["Search", "Direct", "Social", "Email", "Referral"], segments=["Mobile", "Desktop", "Tablet"],
         schema=schema("session_event_id", "user_id", "event_date", "acquisition_channel", "Acquisition channel", "device", "Device", "product_views", "order_value", "items_viewed", "converted", "Conversion"),
         questions=["Which channel-device combinations have strong conversion?", "How does product depth relate to order value?", "Where does revenue concentration create risk?"],
         hypotheses=["Returning direct traffic converts at a higher rate.", "Sessions with more product views have higher order value."], decisions=["Channel investment", "Device experience prioritization", "Merchandising"],
         recommendations=["Prioritize high-impact channel-device journeys for qualitative review.", "Instrument product-view and checkout events consistently before funnel optimization."], value_mean=110, volume_mean=5),
    dict(id="P05", level="Intermediate", slug="banking-campaign-behavior", title="Banking Campaign and Customer Behavior", industry="Banking", seed=105,
         problem_statement="A retail bank needs to improve deposit-campaign efficiency by understanding conversion, contact burden, and segment differences without over-targeting vulnerable customers.",
         stakeholders=["Campaign manager", "Retail banking", "Compliance", "Customer experience"], groups=["Mass market", "Affluent", "Small business", "Youth"], segments=["Phone", "Email", "Branch", "Digital"],
         schema=schema("contact_id", "customer_id", "contact_date", "customer_segment", "Customer segment", "contact_channel", "Contact channel", "contact_duration", "deposit_value", "contact_count", "subscribed", "Subscription"),
         questions=["Which segments convert efficiently?", "Where is contact burden high?", "Do channel differences persist within segments?"],
         hypotheses=["Digital contacts have lower cost per subscription.", "Repeated contact has diminishing association with conversion."], decisions=["Contact policy", "Channel mix", "Experiment design"],
         recommendations=["Set contact-frequency guardrails and track opt-outs.", "Randomize eligible customers across channels before claiming channel effects."], value_mean=2500, value_sigma=0.65, volume_mean=2, driver_mean=8, driver_sd=4),
    dict(id="P06", level="Intermediate", slug="ecommerce-retention-cohorts", title="E-commerce Retention and Cohort Analysis", industry="E-commerce", seed=106, analysis_type="cohort",
         problem_statement="A lifecycle team needs cohort evidence on repeat purchase and customer value to prioritize onboarding and retention experiments.",
         stakeholders=["Lifecycle marketing", "Product", "Finance", "Customer success"], groups=["Organic", "Paid search", "Affiliate", "Email"], segments=["New", "Returning", "Reactivated"],
         schema=schema("order_id", "customer_id", "order_date", "acquisition_source", "Acquisition source", "customer_state", "Customer state", "days_since_prior_order", "order_value", "items", "repeat_order", "Repeat order"),
         questions=["Which acquisition cohorts retain?", "How does repeat value evolve?", "How does censoring affect recent cohorts?"],
         hypotheses=["Organic cohorts retain longer.", "Shorter time to second order is associated with stronger later value."], decisions=["Onboarding investment", "Retention experiment targets", "Cohort monitoring"],
         recommendations=["Compare cohorts only at equal observable ages.", "Test onboarding interventions within acquisition source to reduce mix bias."], value_mean=95, volume_mean=3, outcome_intercept=-0.7),
    dict(id="P07", level="Intermediate", slug="healthcare-utilization", title="Healthcare Utilization Analytics", industry="Healthcare", seed=107,
         problem_statement="A healthcare operations team needs a privacy-safe claims-style analysis of utilization, allowed charges, and service variation to test analytical workflows.",
         stakeholders=["Healthcare operations", "Clinical finance", "Data governance", "Care management"], groups=["Primary care", "Inpatient", "Outpatient", "Emergency", "Specialty"], segments=["Low complexity", "Moderate complexity", "High complexity"],
         schema=schema("claim_id", "beneficiary_id", "service_date", "service_type", "Service type", "complexity_band", "Complexity band", "length_of_stay", "allowed_charge", "service_units", "return_visit_30d", "30-day return visit"),
         questions=["Which service types drive utilization and charges?", "Where do return-visit patterns differ?", "Which findings are invalid for real beneficiaries?"],
         hypotheses=["Higher complexity is associated with higher allowed charges.", "Return-visit rates vary by service type."], decisions=["Analytical workflow design", "Care-review prioritization", "Data acquisition"],
         recommendations=["Use the synthetic results only to validate pipelines and definitions.", "Require clinically reviewed denominators and risk adjustment before operational action."], value_mean=850, value_sigma=0.75, volume_mean=2, driver_mean=3, driver_sd=2),
    dict(id="P08", level="Intermediate", slug="digital-product-funnel", title="Digital Product Funnel Analysis", industry="Digital commerce", seed=108,
         problem_statement="A digital product team needs to identify where high-value sessions stall and which traffic-device segments deserve instrumentation or experience testing.",
         stakeholders=["Product manager", "UX", "Growth", "Engineering"], groups=["Landing", "Browse", "Product", "Checkout"], segments=["New visitor", "Returning visitor", "Campaign visitor"],
         schema=schema("session_id", "visitor_id", "session_date", "deepest_stage", "Deepest stage", "visitor_type", "Visitor type", "engagement_minutes", "page_value", "page_count", "purchased", "Purchase"),
         questions=["Where do sessions stop?", "Which visitor types have stronger completion?", "Is engagement associated with value?"],
         hypotheses=["Returning visitors reach deeper stages.", "Longer engagement is associated with purchase."], decisions=["Funnel instrumentation", "UX experiment priority", "Traffic quality review"],
         recommendations=["Validate stage-event definitions with engineering before optimization.", "Run controlled tests on the largest high-value drop-off rather than changing every stage."], value_mean=45, volume_mean=7, driver_mean=6, driver_sd=3),
    dict(id="P09", level="Advanced", slug="financial-crime-patterns", title="Financial Crime Pattern Exploration", industry="Financial services", seed=109,
         problem_statement="A financial-crime analytics team needs a reproducible synthetic environment to explore transaction velocity, value concentration, and labeled alert patterns without exposing customer data.",
         stakeholders=["AML investigators", "Model risk", "Compliance", "Data engineering"], groups=["Wire", "ACH", "Card", "Cash", "Crypto"], segments=["Consumer", "Business", "Correspondent"],
         schema=schema("transaction_id", "account_id", "transaction_date", "payment_type", "Payment type", "account_type", "Account type", "velocity_score", "transaction_value", "transactions_24h", "laundering_label", "Laundering label"),
         questions=["Which patterns concentrate labeled alerts?", "How heavy-tailed are transaction values?", "Which rules could create excess alerts?"],
         hypotheses=["High velocity is associated with alert labels.", "A small number of payment types drive modeled exposure."], decisions=["Investigator queue design", "Rule review", "Data-quality controls"],
         recommendations=["Optimize for investigator workload and missed-risk tradeoffs, not accuracy alone.", "Review false-alert proxies by account type before threshold changes."], value_mean=9000, value_sigma=1.0, volume_mean=5, driver_mean=55, driver_sd=20, outcome_intercept=-3.0),
    dict(id="P10", level="Advanced", slug="credit-risk-portfolio", title="Credit Risk and Portfolio EDA", industry="Consumer credit", seed=110,
         problem_statement="A credit portfolio team needs to explain where delinquency and default risk concentrate before changing policy or building predictive models.",
         stakeholders=["Credit risk", "Portfolio management", "Fair lending", "Finance"], groups=["Prime", "Near prime", "Subprime"], segments=["Low utilization", "Medium utilization", "High utilization"],
         schema=schema("account_month_id", "account_id", "statement_date", "risk_band", "Risk band", "utilization_band", "Utilization band", "utilization_pct", "balance", "days_past_due", "defaulted", "Default"),
         questions=["Where do defaults and balances concentrate?", "Are delinquency patterns monotonic across bands?", "What features would leak future information?"],
         hypotheses=["Default increases with utilization and delinquency.", "Exposure concentration differs from account-count concentration."], decisions=["Portfolio monitoring", "Policy investigation", "Feature governance"],
         recommendations=["Separate exposure-weighted and account-weighted risk views.", "Audit temporal leakage before any predictive model or policy simulation."], value_mean=4200, value_sigma=0.7, volume_mean=10, driver_mean=52, driver_sd=24, outcome_intercept=-2.2),
    dict(id="P11", level="Advanced", slug="supply-chain-operations", title="Supply Chain Operations Analytics", industry="Supply chain", seed=111,
         problem_statement="An operations leader needs to prioritize the product-region combinations responsible for late delivery, long cycle time, and modeled margin exposure.",
         stakeholders=["Supply chain VP", "Fulfillment", "Procurement", "Finance"], groups=["Apparel", "Electronics", "Home", "Sports"], segments=["North", "South", "East", "West"],
         schema=schema("shipment_line_id", "order_id", "ship_date", "product_family", "Product family", "region", "Region", "cycle_time_days", "order_profit", "units", "late_delivery", "Late delivery"),
         questions=["Where are delays and profit concentrated?", "Which groups show unstable cycle time?", "What process areas deserve root-cause analysis?"],
         hypotheses=["Cycle time is associated with late delivery.", "Profit and service risk concentrate in different groups."], decisions=["Root-cause priority", "SLA review", "Capacity planning"],
         recommendations=["Use a Pareto review that combines service risk and economic impact.", "Validate carrier, facility, and inventory causes before changing SLAs."], value_mean=65, volume_mean=6, driver_mean=7, driver_sd=3, outcome_intercept=-1.0),
    dict(id="P12", level="Advanced", slug="customer-segmentation-value-tiers", title="Customer Segmentation and Value Tiers", industry="Wholesale distribution", seed=112, analysis_type="segmentation",
         problem_statement="A wholesale distributor needs an exploratory segmentation of customer spending and order intensity to design service hypotheses without assuming clusters are permanent truths.",
         stakeholders=["Commercial strategy", "Account management", "Finance", "Customer operations"], groups=["Hospitality", "Retail", "Institutional", "Independent"], segments=["Urban", "Suburban", "Rural"],
         schema=schema("customer_period_id", "customer_id", "period_date", "channel", "Channel", "region_type", "Region type", "fresh_share_pct", "annual_spend", "order_frequency", "high_value_flag", "High-value flag"),
         questions=["Which spending and frequency profiles emerge?", "Are clusters stable?", "How should service hypotheses differ by profile?"],
         hypotheses=["Spending and order frequency form distinct profiles.", "Channel mix explains part of segment differences."], decisions=["Service design", "Account coverage", "Segmentation research"],
         recommendations=["Stress-test cluster count and initialization before labeling segments.", "Use clusters to generate service hypotheses, then validate with customer outcomes."], value_mean=18000, value_sigma=0.8, volume_mean=12, driver_mean=35, driver_sd=18, outcome_intercept=-1.0),
    dict(id="P13", level="Expert", slug="ai-adoption-value-realization", title="AI Tool Adoption and Value Realization", industry="Technology", seed=113,
         problem_statement="A product and technology leadership team needs to distinguish AI adoption from realized value and identify trust, governance, and cost barriers across user groups.",
         stakeholders=["AI product leader", "Engineering leadership", "Finance", "Risk and compliance"], groups=["Software engineering", "Data", "Product", "Operations", "Leadership"], segments=["Individual contributor", "Manager", "Executive"],
         schema=schema("survey_response_id", "respondent_id", "response_date", "job_family", "Job family", "role_level", "Role level", "weekly_ai_hours", "reported_value_score", "tools_used", "frequent_ai_use", "Frequent AI use"),
         questions=["Who adopts AI tools frequently?", "Where is value reported?", "Which barriers require product versus governance action?"],
         hypotheses=["Adoption and reported value differ by role.", "High use does not always imply trust or value."], decisions=["Enablement investment", "Product roadmap", "Governance"],
         recommendations=["Separate adoption, value, trust, and cost metrics in executive reporting.", "Validate self-reported value with workflow telemetry and pre/post baselines."], value_mean=63, volume_mean=4, driver_mean=7, driver_sd=5, outcome_intercept=0.0),
    dict(id="P14", level="Expert", slug="digital-banking-service-risk", title="Digital Banking Service Failure and Retention Risk", industry="Consumer banking", seed=114,
         problem_statement="A digital banking operations team needs to prioritize complaint themes and response failures while avoiding misleading company rankings without customer denominators.",
         stakeholders=["Digital banking", "Complaint operations", "Compliance", "Customer experience"], groups=["Payments", "Cards", "Deposits", "Transfers", "Authentication"], segments=["Mobile", "Web", "Contact center"],
         schema=schema("complaint_id", "consumer_case_id", "received_date", "product_issue", "Product issue", "submission_channel", "Submission channel", "response_days", "modeled_retention_value", "contacts", "untimely_response", "Untimely response"),
         questions=["Which themes are growing?", "Where are responses slow?", "What conclusions require market-share denominators?"],
         hypotheses=["Authentication complaints have different response times.", "Repeated contacts are associated with untimely response."], decisions=["Operational investigation", "Issue taxonomy", "Response SLA"],
         recommendations=["Prioritize theme-level process failures, not raw company rankings.", "Add active-customer denominators before comparing complaint rates across products."], value_mean=380, value_sigma=0.7, volume_mean=2, driver_mean=8, driver_sd=5, outcome_intercept=-1.2),
    dict(id="P15", level="Expert", slug="legal-ai-review-operations", title="Legal AI Document Review Operations", industry="Legal technology", seed=115,
         problem_statement="A legal AI product team needs to estimate clause-review workload, rare-clause QA coverage, and human capacity without treating automated labels as final legal judgments.",
         stakeholders=["Legal operations", "Product", "Machine learning", "Quality assurance"], groups=["Termination", "Liability", "Change of control", "Confidentiality", "Assignment"], segments=["Commercial", "Employment", "Licensing", "Services"],
         schema=schema("clause_annotation_id", "contract_id", "review_date", "clause_type", "Clause type", "contract_type", "Contract type", "review_minutes", "modeled_review_cost", "clause_count", "qa_issue", "QA issue"),
         questions=["Which clause types drive workload?", "Where is QA issue prevalence highest?", "How should rare clauses be sampled?"],
         hypotheses=["Rare clauses require disproportionate QA effort.", "Review time varies by contract type."], decisions=["QA sampling", "Human review capacity", "Product prioritization"],
         recommendations=["Guarantee minimum QA coverage for rare, high-consequence clauses.", "Keep qualified legal review as the final decision point and monitor annotation drift."], value_mean=95, volume_mean=4, driver_mean=18, driver_sd=9, outcome_intercept=-2.0),
    dict(id="P16", level="Expert", slug="product-experimentation-uplift", title="Product Experimentation and Uplift Analysis", industry="Advertising technology", seed=116, analysis_type="experiment", treatment_effect=0.32,
         problem_statement="A growth team needs to decide whether a randomized advertising treatment improves conversion enough to justify rollout and which segments require follow-up experiments.",
         stakeholders=["Growth product", "Marketing science", "Finance", "Experimentation platform"], groups=["Search", "Social", "Display", "Video"], segments=["New", "Returning", "High intent"],
         schema=schema("experiment_event_id", "user_id", "assignment_date", "channel", "Channel", "audience_segment", "Audience segment", "prior_engagement_score", "conversion_value", "impressions", "converted", "Conversion", "treatment"),
         questions=["Is assignment balanced?", "What is the absolute treatment effect?", "Does practical value justify rollout?"],
         hypotheses=["Treatment increases conversion.", "Effect size differs by pre-specified audience segment."], decisions=["Rollout", "Experiment iteration", "Budget allocation"],
         recommendations=["Base rollout on the pre-specified absolute effect and interval, not p-value alone.", "Treat segment effects as exploratory unless powered and adjusted for multiplicity."], value_mean=32, volume_mean=8, driver_mean=55, driver_sd=20, outcome_intercept=-2.0),
]


def project_path(project):
    return ROOT / "projects" / LEVEL_DIRS[project["level"]] / f"{project['id']}-{project['slug']}"


def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def build_readme(project):
    s = project["schema"]
    stakeholder_text = ", ".join(project["stakeholders"])
    questions = "\n".join(f"{i}. {q}" for i, q in enumerate(project["questions"], 1))
    hypotheses = "\n".join(f"- {h}" for h in project["hypotheses"])
    decisions = "\n".join(f"- {d}" for d in project["decisions"])
    return f"""# {project['id']}: {project['title']}

**Level:** {project['level']}  
**Industry:** {project['industry']}  
**Data:** deterministic synthetic data generated in this repository

## Business problem

{project['problem_statement']}

**Stakeholders:** {stakeholder_text}

## Analytical questions

{questions}

## Hypotheses to investigate

{hypotheses}

These are exploratory hypotheses. Except for P16's randomized synthetic treatment, the project does not make causal claims.

## Decisions supported

{decisions}

## KPI definitions

| KPI | Definition |
|---|---|
| Total modeled value | Sum of `{s['value_col']}` across in-scope records |
| Total modeled impact | Sum of `{s['value_col']} × {s['volume_col']}` |
| {s['outcome_label']} rate | Mean of binary `{s['outcome_col']}` across in-scope records |
| Active entities | Distinct count of `{s['entity_id_col']}` |
| Group concentration | Share of total modeled impact by `{s['group_col']}` |

## Repository contents

- `data/raw/synthetic_data.csv` — generated input with no real people or organizations
- `data/processed/` — calculated QA, KPI, trend, and method-specific outputs
- `src/generate_data.py` — reproducible data generator entry point
- `src/analysis.py` — full analysis entry point
- `sql/` — PostgreSQL quality, exploration, and business queries
- `notebooks/eda_analysis.ipynb` — narrative runnable notebook
- `visualizations/` — generated SVG charts
- `reports/executive_summary.md` — evidence-backed decision summary
- `data_dictionary.md` — field definitions and grain

## Run locally

From this project directory:

```bash
python src/generate_data.py
python src/analysis.py
```

Or run the full portfolio from the repository root:

```bash
python run_all.py
python -m unittest discover -s tests
```

## Integrity statement

The committed data is synthetic, generated with seed `{project['seed']}`, and intended for portfolio demonstration. Findings in the executive summary are calculated from that data. They are not claims about a real company, customer population, patient population, workforce, or market.
"""


def build_dictionary(project):
    s = project["schema"]
    definitions = [
        (s["event_id_col"], "string", "Unique synthetic record identifier"),
        (s["entity_id_col"], "string", "Synthetic entity identifier; can repeat across records"),
        (s["date_col"], "date", "Synthetic event date"),
        (s["group_col"], "category", f"Primary {s['group_label'].lower()} dimension"),
        (s["segment_col"], "category", f"Secondary {s['segment_label'].lower()} dimension"),
        (s["driver_col"], "number", "Continuous exploratory driver with approximately 1% intentional missingness"),
        (s["value_col"], "number", "Positive modeled economic, performance, or operational value"),
        (s["volume_col"], "integer", "Positive modeled activity or exposure count"),
        (s["outcome_col"], "0/1", f"Binary indicator for {s['outcome_label'].lower()}"),
    ]
    if s.get("treatment_col"):
        definitions.append((s["treatment_col"], "0/1", "Randomized synthetic treatment assignment"))
    rows = "\n".join(f"| `{name}` | {dtype} | {definition} |" for name, dtype, definition in definitions)
    return f"""# Data Dictionary

**Grain:** one synthetic event, observation, claim, response, annotation, or period record per row, as defined by `{s['event_id_col']}`.

| Field | Type | Definition |
|---|---|---|
{rows}

Missingness is deliberately introduced only in `{s['driver_col']}` to support data-quality analysis. No field contains real personal or organizational data.
"""


def build_sql(project):
    s = project["schema"]
    quality = f"""-- Business question: Is the loaded synthetic table complete and structurally usable?
-- Expected output: one row of control counts. Any nonzero duplicate or invalid-outcome count requires investigation.
SELECT
    COUNT(*) AS row_count,
    COUNT(DISTINCT {s['event_id_col']}) AS distinct_event_ids,
    COUNT(*) - COUNT(DISTINCT {s['event_id_col']}) AS duplicate_event_ids,
    COUNT(*) FILTER (WHERE {s['driver_col']} IS NULL) AS missing_driver_values,
    COUNT(*) FILTER (WHERE {s['outcome_col']} NOT IN (0, 1)) AS invalid_outcomes
FROM project_events;
"""
    exploration = f"""-- Business question: How do scale, value, and outcome rate differ by {s['group_label'].lower()}?
-- Expected output: one row per {s['group_col']}, ordered by modeled impact.
SELECT
    {s['group_col']},
    COUNT(*) AS records,
    COUNT(DISTINCT {s['entity_id_col']}) AS entities,
    SUM({s['value_col']}) AS total_value,
    SUM({s['volume_col']}) AS total_volume,
    SUM({s['value_col']} * {s['volume_col']}) AS modeled_impact,
    AVG({s['outcome_col']}::numeric) AS outcome_rate
FROM project_events
GROUP BY {s['group_col']}
ORDER BY modeled_impact DESC;
"""
    business = f"""-- Business question: Which group-segment combinations combine high impact with high observed outcome rates?
-- Logic: aggregate at a decision-relevant grain, then rank groups within each segment.
WITH segment_kpis AS (
    SELECT
        {s['segment_col']},
        {s['group_col']},
        COUNT(*) AS records,
        SUM({s['value_col']} * {s['volume_col']}) AS modeled_impact,
        AVG({s['outcome_col']}::numeric) AS outcome_rate
    FROM project_events
    GROUP BY {s['segment_col']}, {s['group_col']}
), ranked AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY {s['segment_col']} ORDER BY modeled_impact DESC) AS impact_rank
    FROM segment_kpis
)
SELECT *
FROM ranked
WHERE impact_rank <= 3
ORDER BY {s['segment_col']}, impact_rank;

-- Performance note: index the date, entity, group, and segment fields for repeated analysis on large tables.
CREATE INDEX IF NOT EXISTS idx_project_events_date ON project_events ({s['date_col']});
CREATE INDEX IF NOT EXISTS idx_project_events_entity ON project_events ({s['entity_id_col']});
"""
    if s.get("treatment_col"):
        business += f"""

-- Randomized experiment estimate: absolute difference in conversion rates.
SELECT {s['treatment_col']}, COUNT(*) AS n, AVG({s['outcome_col']}::numeric) AS outcome_rate
FROM project_events
GROUP BY {s['treatment_col']}
ORDER BY {s['treatment_col']};
"""
    return quality, exploration, business


def build_notebook(project, path):
    notebook = {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": [f"# {project['title']}\n", "\n", "This notebook executes the committed synthetic-data analysis and exposes the generated KPI tables for inspection.\n"]},
            {"cell_type": "markdown", "metadata": {}, "source": ["## Integrity boundary\n", "All records are synthetic. Observational differences are descriptive associations, not causal effects.\n"]},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["from pathlib import Path\n", "import sys\n", "project_dir = Path.cwd().resolve().parent if Path.cwd().name == 'notebooks' else Path.cwd().resolve()\n", "repo_root = project_dir.parents[2]\n", "sys.path.insert(0, str(repo_root / 'src'))\n", "from portfolio_core import run_project\n", "results = run_project(project_dir, regenerate=False)\n", "results\n"]},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["import pandas as pd\n", "pd.read_csv(project_dir / 'data' / 'processed' / 'group_kpis.csv')\n"]},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["pd.read_csv(project_dir / 'data' / 'processed' / 'monthly_kpis.csv').head()\n"]},
        ],
        "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.10+"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    write_text(path, json.dumps(notebook, indent=2))


def build_project(project):
    path = project_path(project)
    path.mkdir(parents=True, exist_ok=True)
    config = {k: v for k, v in project.items() if k not in {"slug"}}
    config.setdefault("rows", 2400)
    config.setdefault("entities", 520)
    config.setdefault("start_date", "2024-01-01")
    config.setdefault("days", 730)
    config.setdefault("analysis_type", "standard")
    write_text(path / "project_config.json", json.dumps(config, indent=2))
    write_text(path / "README.md", build_readme(project))
    write_text(path / "data_dictionary.md", build_dictionary(project))

    runner_common = """from pathlib import Path
import sys

PROJECT_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))
from portfolio_core import run_project
"""
    write_text(path / "src" / "generate_data.py", runner_common + "\nif __name__ == \"__main__\":\n    run_project(PROJECT_DIR, regenerate=True)\n    print(f\"Generated {PROJECT_DIR / 'data/raw/synthetic_data.csv'}\")")
    write_text(path / "src" / "analysis.py", runner_common + "\nif __name__ == \"__main__\":\n    result = run_project(PROJECT_DIR, regenerate=False)\n    print(result)\n")

    quality, exploration, business = build_sql(project)
    write_text(path / "sql" / "01_data_quality.sql", quality)
    write_text(path / "sql" / "02_exploration.sql", exploration)
    write_text(path / "sql" / "03_business_analysis.sql", business)
    build_notebook(project, path / "notebooks" / "eda_analysis.ipynb")
    result = run_project(path, regenerate=True)
    return path, result


def build_root(manifest):
    table_rows = "\n".join(f"| {row['sequence']} | {row['project_id']} | {row['level']} | [{row['title']}]({row['path']}) | {row['industry']} |" for row in manifest)
    readme = f"""# EDA and Data Analytics Portfolio

Sixteen evidence-driven exploratory data analysis projects spanning retail, education, workforce, e-commerce, banking, healthcare, financial crime, credit risk, supply chain, AI adoption, legal technology, and experimentation.

Every project includes a detailed business problem, deterministic synthetic data, Python analysis, PostgreSQL queries, a runnable notebook, calculated visualizations, and an executive summary. Synthetic results are clearly labeled and never presented as real organizational findings.

## Portfolio map

| Seq. | ID | Level | Project | Industry |
|---:|---|---|---|---|
{table_rows}

## Run the entire portfolio

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_all.py --regenerate
python -m unittest discover -s tests
```

## Project contract

Each project contains:

- `README.md` with problem, stakeholders, analytical questions, hypotheses, KPIs, and decisions
- `data/raw/synthetic_data.csv` generated from a fixed seed
- `src/generate_data.py` and `src/analysis.py`
- three PostgreSQL scripts for quality, exploration, and business analysis
- `notebooks/eda_analysis.ipynb`
- processed KPI tables and SVG visualizations
- `reports/executive_summary.md` using observation → evidence → interpretation → implication → action → validation

## Integrity and limitations

- The data is synthetic and contains no real people or organizations.
- Projects are exploratory. They distinguish association from causation.
- P16 uses randomized synthetic treatment; its causal interpretation applies only to the generator, not to a real product.
- Replacing synthetic inputs with real data requires governance, privacy review, metric validation, and stakeholder approval.

## License

Code and original documentation are released under the MIT License. Synthetic datasets are generated by this repository and may be reused with attribution. Third-party public datasets listed in the planning roadmap are not redistributed here.
"""
    write_text(ROOT / "README.md", readme)
    write_text(ROOT / "requirements.txt", "pandas>=2.0,<3.0\nnumpy>=1.26,<3.0")
    write_text(ROOT / ".gitignore", ".venv/\n__pycache__/\n*.py[cod]\n.ipynb_checkpoints/\n.DS_Store\n")
    write_text(ROOT / "LICENSE", "MIT License\n\nCopyright (c) 2026\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
    write_text(ROOT / "run_all.py", """from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from portfolio_core import run_project

parser = argparse.ArgumentParser()
parser.add_argument("--regenerate", action="store_true")
args = parser.parse_args()

results = {}
for config_path in sorted((ROOT / "projects").glob("**/project_config.json")):
    project_dir = config_path.parent
    config = json.loads(config_path.read_text())
    print(f"Running {config['id']}: {config['title']}")
    results[config['id']] = run_project(project_dir, regenerate=args.regenerate)
print(f"Completed {len(results)} projects.")
""")
    write_text(ROOT / "tests" / "test_portfolio.py", """import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PortfolioTest(unittest.TestCase):
    def setUp(self):
        self.configs = sorted((ROOT / "projects").glob("**/project_config.json"))

    def test_all_sixteen_projects_exist(self):
        self.assertEqual(len(self.configs), 16)

    def test_required_artifacts_and_outputs(self):
        required = ["README.md", "data_dictionary.md", "data/raw/synthetic_data.csv", "data/processed/overall_kpis.csv", "src/generate_data.py", "src/analysis.py", "sql/01_data_quality.sql", "sql/02_exploration.sql", "sql/03_business_analysis.sql", "notebooks/eda_analysis.ipynb", "visualizations/monthly_impact.svg", "visualizations/outcome_rate_by_group.svg", "reports/executive_summary.md"]
        for config_path in self.configs:
            project = config_path.parent
            for relative in required:
                self.assertTrue((project / relative).exists(), f"Missing {project / relative}")

    def test_kpis_are_calculated(self):
        for config_path in self.configs:
            project = config_path.parent
            with (project / "data/processed/overall_kpis.csv").open() as handle:
                row = next(csv.DictReader(handle))
            self.assertGreater(int(float(row["records"])), 0)
            self.assertGreater(float(row["total_impact"]), 0)
            self.assertGreaterEqual(float(row["outcome_rate"]), 0)
            self.assertLessEqual(float(row["outcome_rate"]), 1)

    def test_notebooks_are_valid_json(self):
        for config_path in self.configs:
            notebook = config_path.parent / "notebooks/eda_analysis.ipynb"
            data = json.loads(notebook.read_text())
            self.assertEqual(data["nbformat"], 4)

if __name__ == "__main__":
    unittest.main()
""")


def main():
    manifest = []
    for sequence, project in enumerate(PROJECTS, 1):
        path, result = build_project(project)
        manifest.append({
            "sequence": sequence,
            "project_id": project["id"],
            "level": project["level"],
            "title": project["title"],
            "industry": project["industry"],
            "path": path.relative_to(ROOT).as_posix(),
            "rows": result["overall"]["records"],
            "entities": result["overall"]["entities"],
            "top_impact_group": result["top_impact_group"],
        })
        print(f"Built {project['id']}: {project['title']}")
    build_root(manifest)
    write_manifest(manifest, ROOT / "portfolio_manifest.csv")
    print(f"Built {len(manifest)} projects in {ROOT}")


if __name__ == "__main__":
    main()
