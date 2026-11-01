"""Shared, auditable engine for the synthetic EDA portfolio.

Every project supplies a JSON configuration describing its business vocabulary,
dimensions, measures, KPIs, and decision context. This module generates a
deterministic synthetic dataset and executes the same reproducible quality,
descriptive, segmentation/cohort, and statistical workflow with project-specific
column names. It deliberately avoids predictive or causal claims.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from statistics import NormalDist
from typing import Any

import numpy as np
import pandas as pd


def _sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -25, 25)))


def load_config(project_dir: Path) -> dict[str, Any]:
    with (project_dir / "project_config.json").open(encoding="utf-8") as handle:
        return json.load(handle)


def generate_dataset(project_dir: Path, config: dict[str, Any]) -> Path:
    """Generate deterministic, clearly labeled synthetic business-event data."""
    schema = config["schema"]
    rows = int(config.get("rows", 2400))
    entities = int(config.get("entities", max(200, rows // 5)))
    rng = np.random.default_rng(int(config["seed"]))

    start = pd.Timestamp(config.get("start_date", "2024-01-01"))
    days = int(config.get("days", 730))
    dates = start + pd.to_timedelta(rng.integers(0, days, size=rows), unit="D")
    group_idx = rng.choice(len(config["groups"]), size=rows, p=config.get("group_probs"))
    segment_idx = rng.choice(len(config["segments"]), size=rows, p=config.get("segment_probs"))
    groups = np.array(config["groups"], dtype=object)[group_idx]
    segments = np.array(config["segments"], dtype=object)[segment_idx]

    entity_ids = rng.integers(1, entities + 1, size=rows)
    event_ids = np.arange(1, rows + 1)
    driver = np.clip(rng.normal(config.get("driver_mean", 50), config.get("driver_sd", 14), rows), 0, None)
    group_effect = (group_idx - np.mean(group_idx)) * float(config.get("group_effect", 0.18))
    segment_effect = (segment_idx - np.mean(segment_idx)) * float(config.get("segment_effect", 0.12))

    treatment = None
    treatment_effect = 0.0
    if schema.get("treatment_col"):
        treatment = rng.binomial(1, 0.5, rows)
        treatment_effect = treatment * float(config.get("treatment_effect", 0.22))

    latent = (
        float(config.get("outcome_intercept", -1.45))
        + group_effect
        + segment_effect
        + 0.035 * ((driver - driver.mean()) / max(driver.std(), 1))
        + treatment_effect
        + rng.normal(0, 0.2, rows)
    )
    outcome = rng.binomial(1, _sigmoid(latent))

    base_value = float(config.get("value_mean", 120))
    value = rng.lognormal(mean=math.log(base_value), sigma=float(config.get("value_sigma", 0.45)), size=rows)
    value *= 1 + 0.07 * group_idx + 0.04 * segment_idx + 0.05 * outcome
    volume_mean = float(config.get("volume_mean", 5))
    volume = rng.poisson(np.clip(volume_mean * (1 + 0.08 * group_idx + 0.05 * outcome), 0.2, None), rows) + 1

    frame = pd.DataFrame(
        {
            schema["event_id_col"]: [f"{config['id']}-E{x:06d}" for x in event_ids],
            schema["entity_id_col"]: [f"{config['id']}-C{x:05d}" for x in entity_ids],
            schema["date_col"]: dates.strftime("%Y-%m-%d"),
            schema["group_col"]: groups,
            schema["segment_col"]: segments,
            schema["driver_col"]: np.round(driver, 2),
            schema["value_col"]: np.round(value, 2),
            schema["volume_col"]: volume.astype(int),
            schema["outcome_col"]: outcome.astype(int),
        }
    )
    if treatment is not None:
        frame[schema["treatment_col"]] = treatment.astype(int)

    # A small, reproducible missingness pattern gives every project a genuine QA task.
    missing_rows = rng.choice(rows, size=max(1, rows // 100), replace=False)
    frame.loc[missing_rows, schema["driver_col"]] = np.nan

    output = project_dir / "data" / "raw" / "synthetic_data.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output, index=False)
    return output


def _rate_interval(successes: int, total: int) -> tuple[float, float, float]:
    if total == 0:
        return (math.nan, math.nan, math.nan)
    p = successes / total
    z = 1.96
    denominator = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denominator
    margin = z * math.sqrt((p * (1 - p) + z * z / (4 * total)) / total) / denominator
    return p, max(0.0, center - margin), min(1.0, center + margin)


def _difference_in_rates(frame: pd.DataFrame, treatment_col: str, outcome_col: str) -> dict[str, float]:
    treated = frame.loc[frame[treatment_col] == 1, outcome_col].astype(float)
    control = frame.loc[frame[treatment_col] == 0, outcome_col].astype(float)
    p1, p0 = treated.mean(), control.mean()
    effect = p1 - p0
    se = math.sqrt(p1 * (1 - p1) / len(treated) + p0 * (1 - p0) / len(control))
    z_score = effect / se if se else math.nan
    p_value = 2 * (1 - NormalDist().cdf(abs(z_score))) if math.isfinite(z_score) else math.nan
    return {
        "treated_n": int(len(treated)),
        "control_n": int(len(control)),
        "treated_rate": float(p1),
        "control_rate": float(p0),
        "absolute_effect": float(effect),
        "ci_low": float(effect - 1.96 * se),
        "ci_high": float(effect + 1.96 * se),
        "z_score": float(z_score),
        "p_value": float(p_value),
    }


def _kmeans_two_features(frame: pd.DataFrame, columns: list[str], seed: int, k: int = 4) -> pd.Series:
    values = frame[columns].fillna(frame[columns].median()).astype(float).to_numpy()
    means = values.mean(axis=0)
    stds = values.std(axis=0)
    scaled = (values - means) / np.where(stds == 0, 1, stds)
    rng = np.random.default_rng(seed)
    centers = scaled[rng.choice(len(scaled), size=k, replace=False)]
    labels = np.zeros(len(scaled), dtype=int)
    for _ in range(50):
        distances = ((scaled[:, None, :] - centers[None, :, :]) ** 2).sum(axis=2)
        next_labels = distances.argmin(axis=1)
        if np.array_equal(labels, next_labels):
            break
        labels = next_labels
        for cluster in range(k):
            if np.any(labels == cluster):
                centers[cluster] = scaled[labels == cluster].mean(axis=0)
    return pd.Series(labels + 1, index=frame.index, name="exploratory_cluster")


def _write_line_chart(data: pd.DataFrame, x_col: str, y_col: str, title: str, output: Path) -> None:
    width, height, pad = 900, 420, 70
    values = data[y_col].astype(float).to_numpy()
    if len(values) == 0:
        return
    ymin, ymax = float(values.min()), float(values.max())
    span = ymax - ymin or 1.0
    points = []
    for i, value in enumerate(values):
        x = pad + i * (width - 2 * pad) / max(1, len(values) - 1)
        y = height - pad - (value - ymin) * (height - 2 * pad) / span
        points.append(f"{x:.1f},{y:.1f}")
    labels = "".join(
        f'<text x="{pad + i * (width - 2 * pad) / max(1, len(values)-1):.1f}" y="{height-25}" font-size="10" text-anchor="middle">{str(label)[:7]}</text>'
        for i, label in enumerate(data[x_col]) if i % max(1, len(data) // 8) == 0
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
<rect width="100%" height="100%" fill="white"/><text x="{pad}" y="32" font-family="Arial" font-size="20" font-weight="bold">{title}</text>
<line x1="{pad}" y1="{height-pad}" x2="{width-pad}" y2="{height-pad}" stroke="#8A99A8"/><line x1="{pad}" y1="{pad}" x2="{pad}" y2="{height-pad}" stroke="#8A99A8"/>
<polyline fill="none" stroke="#1769AA" stroke-width="3" points="{' '.join(points)}"/>{labels}
<text x="15" y="{pad}" font-family="Arial" font-size="11">{ymax:,.1f}</text><text x="15" y="{height-pad}" font-family="Arial" font-size="11">{ymin:,.1f}</text></svg>'''
    output.write_text(svg, encoding="utf-8")


def _write_bar_chart(data: pd.DataFrame, label_col: str, value_col: str, title: str, output: Path) -> None:
    width, height, pad = 900, 430, 80
    values = data[value_col].astype(float).to_numpy()
    max_value = float(values.max()) if len(values) else 1.0
    bar_width = (width - 2 * pad) / max(1, len(values)) * 0.65
    bars = []
    for i, (_, row) in enumerate(data.iterrows()):
        x = pad + (i + 0.18) * (width - 2 * pad) / len(values)
        h = float(row[value_col]) / max(max_value, 1e-9) * (height - 2 * pad)
        y = height - pad - h
        bars.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_width:.1f}" height="{h:.1f}" fill="#4C9F70"/>')
        bars.append(f'<text x="{x+bar_width/2:.1f}" y="{height-45}" font-size="10" text-anchor="middle">{str(row[label_col])[:15]}</text>')
        bars.append(f'<text x="{x+bar_width/2:.1f}" y="{max(55,y-7):.1f}" font-size="10" text-anchor="middle">{float(row[value_col]):.1%}</text>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"><rect width="100%" height="100%" fill="white"/>
<text x="{pad}" y="32" font-family="Arial" font-size="20" font-weight="bold">{title}</text><line x1="{pad}" y1="{height-pad}" x2="{width-pad}" y2="{height-pad}" stroke="#8A99A8"/>{''.join(bars)}</svg>'''
    output.write_text(svg, encoding="utf-8")


def analyze_project(project_dir: Path, config: dict[str, Any]) -> dict[str, Any]:
    schema = config["schema"]
    raw_path = project_dir / "data" / "raw" / "synthetic_data.csv"
    frame = pd.read_csv(raw_path)
    frame[schema["date_col"]] = pd.to_datetime(frame[schema["date_col"]], errors="coerce")
    numeric_cols = [schema["driver_col"], schema["value_col"], schema["volume_col"], schema["outcome_col"]]
    frame[numeric_cols] = frame[numeric_cols].apply(pd.to_numeric, errors="coerce")
    frame["impact_value"] = frame[schema["value_col"]] * frame[schema["volume_col"]]
    frame["month"] = frame[schema["date_col"]].dt.to_period("M").astype(str)

    processed = project_dir / "data" / "processed"
    visuals = project_dir / "visualizations"
    reports = project_dir / "reports"
    for folder in (processed, visuals, reports):
        folder.mkdir(parents=True, exist_ok=True)

    quality = pd.DataFrame(
        {
            "metric": ["rows", "columns", "duplicate_event_ids", "missing_cells", "invalid_dates", "outcome_values_outside_0_1"],
            "value": [
                len(frame),
                len(frame.columns),
                int(frame[schema["event_id_col"]].duplicated().sum()),
                int(frame.isna().sum().sum()),
                int(frame[schema["date_col"]].isna().sum()),
                int((~frame[schema["outcome_col"]].isin([0, 1])).sum()),
            ],
        }
    )
    quality.to_csv(processed / "data_quality_report.csv", index=False)

    successes = int(frame[schema["outcome_col"]].sum())
    rate, ci_low, ci_high = _rate_interval(successes, len(frame))
    overall = {
        "records": int(len(frame)),
        "entities": int(frame[schema["entity_id_col"]].nunique()),
        "start_date": frame[schema["date_col"]].min().date().isoformat(),
        "end_date": frame[schema["date_col"]].max().date().isoformat(),
        "total_value": float(frame[schema["value_col"]].sum()),
        "total_volume": float(frame[schema["volume_col"]].sum()),
        "total_impact": float(frame["impact_value"].sum()),
        "average_value": float(frame[schema["value_col"]].mean()),
        "average_volume": float(frame[schema["volume_col"]].mean()),
        "outcome_rate": float(rate),
        "outcome_ci_low": float(ci_low),
        "outcome_ci_high": float(ci_high),
        "value_volume_correlation": float(frame[[schema["value_col"], schema["volume_col"]]].corr().iloc[0, 1]),
    }

    group_summary = (
        frame.groupby(schema["group_col"], dropna=False)
        .agg(
            records=(schema["event_id_col"], "count"),
            entities=(schema["entity_id_col"], "nunique"),
            total_value=(schema["value_col"], "sum"),
            total_volume=(schema["volume_col"], "sum"),
            total_impact=("impact_value", "sum"),
            outcome_rate=(schema["outcome_col"], "mean"),
        )
        .reset_index()
        .sort_values("total_impact", ascending=False)
    )
    group_summary.to_csv(processed / "group_kpis.csv", index=False)

    segment_summary = (
        frame.groupby(schema["segment_col"], dropna=False)
        .agg(records=(schema["event_id_col"], "count"), total_impact=("impact_value", "sum"), outcome_rate=(schema["outcome_col"], "mean"))
        .reset_index()
        .sort_values("total_impact", ascending=False)
    )
    segment_summary.to_csv(processed / "segment_kpis.csv", index=False)

    monthly = (
        frame.groupby("month")
        .agg(records=(schema["event_id_col"], "count"), total_value=(schema["value_col"], "sum"), total_impact=("impact_value", "sum"), outcome_rate=(schema["outcome_col"], "mean"))
        .reset_index()
        .sort_values("month")
    )
    monthly.to_csv(processed / "monthly_kpis.csv", index=False)

    method_outputs: dict[str, Any] = {}
    if config.get("analysis_type") == "cohort":
        first_month = frame.groupby(schema["entity_id_col"])["month"].min().rename("cohort_month")
        cohort_frame = frame.join(first_month, on=schema["entity_id_col"])
        cohort = cohort_frame.groupby(["cohort_month", "month"])[schema["entity_id_col"]].nunique().reset_index(name="active_entities")
        cohort_sizes = cohort.groupby("cohort_month")["active_entities"].first().rename("cohort_size")
        cohort = cohort.join(cohort_sizes, on="cohort_month")
        cohort["retention_rate"] = cohort["active_entities"] / cohort["cohort_size"]
        cohort.to_csv(processed / "cohort_retention.csv", index=False)
        method_outputs["cohorts"] = int(cohort["cohort_month"].nunique())
    elif config.get("analysis_type") == "segmentation":
        frame["exploratory_cluster"] = _kmeans_two_features(frame, [schema["value_col"], schema["volume_col"]], int(config["seed"]))
        clusters = frame.groupby("exploratory_cluster").agg(records=(schema["event_id_col"], "count"), average_value=(schema["value_col"], "mean"), average_volume=(schema["volume_col"], "mean"), outcome_rate=(schema["outcome_col"], "mean")).reset_index()
        clusters.to_csv(processed / "exploratory_clusters.csv", index=False)
        method_outputs["clusters"] = int(clusters.shape[0])
    elif schema.get("treatment_col"):
        experiment = _difference_in_rates(frame, schema["treatment_col"], schema["outcome_col"])
        pd.DataFrame([experiment]).to_csv(processed / "experiment_effect.csv", index=False)
        method_outputs["experiment"] = experiment

    pd.DataFrame([overall]).to_csv(processed / "overall_kpis.csv", index=False)
    _write_line_chart(monthly, "month", "total_impact", f"{config['title']}: monthly impact", visuals / "monthly_impact.svg")
    _write_bar_chart(group_summary, schema["group_col"], "outcome_rate", f"{config['title']}: outcome rate by {schema['group_label']}", visuals / "outcome_rate_by_group.svg")

    top_impact = group_summary.iloc[0]
    top_outcome = group_summary.sort_values("outcome_rate", ascending=False).iloc[0]
    first_period = float(monthly.head(min(3, len(monthly)))["total_impact"].mean())
    last_period = float(monthly.tail(min(3, len(monthly)))["total_impact"].mean())
    trend_change = (last_period / first_period - 1) if first_period else math.nan

    executive = [
        f"# Executive Summary: {config['title']}",
        "",
        "## Decision context",
        "",
        config["problem_statement"],
        "",
        "All findings below come from the repository's deterministic synthetic dataset. They demonstrate the analytical workflow and must not be presented as real organizational results.",
        "",
        "## Headline findings",
        "",
        f"1. **Portfolio scale.** The analysis covers {overall['records']:,} records and {overall['entities']:,} unique entities from {overall['start_date']} through {overall['end_date']}. Total modeled impact is {overall['total_impact']:,.0f}.",
        f"2. **Highest-impact group.** `{top_impact[schema['group_col']]}` contributes the most modeled impact ({top_impact['total_impact']:,.0f}) across {int(top_impact['records']):,} records.",
        f"3. **Highest outcome rate.** `{top_outcome[schema['group_col']]}` has the highest {schema['outcome_label'].lower()} rate at {top_outcome['outcome_rate']:.1%}. The portfolio-wide rate is {overall['outcome_rate']:.1%} (95% Wilson interval {overall['outcome_ci_low']:.1%}–{overall['outcome_ci_high']:.1%}).",
        f"4. **Recent movement.** Average modeled impact in the latest three months is {trend_change:+.1%} versus the first three months in the synthetic observation window.",
    ]
    if "experiment" in method_outputs:
        exp = method_outputs["experiment"]
        executive.append(f"5. **Experiment estimate.** Treatment changes the observed outcome rate by {exp['absolute_effect']:+.2%} (95% interval {exp['ci_low']:+.2%} to {exp['ci_high']:+.2%}, two-sided p={exp['p_value']:.3f}). This estimate is causal only because the synthetic generator randomizes treatment.")
    if "clusters" in method_outputs:
        executive.append(f"5. **Exploratory segmentation.** A four-cluster solution was produced from standardized value and volume fields. Clusters are descriptive working groups, not natural or permanent customer types.")
    if "cohorts" in method_outputs:
        executive.append(f"5. **Cohort coverage.** The retention output spans {method_outputs['cohorts']} acquisition cohorts. Later cohorts have shorter observable follow-up and should not be compared at unavailable ages.")

    executive.extend(
        [
            "",
            "## Observation → evidence → implication → action → validation",
            "",
            f"- **Observation:** `{top_impact[schema['group_col']]}` leads modeled impact. **Evidence:** {top_impact['total_impact']:,.0f} impact across {int(top_impact['records']):,} records. **Interpretation:** this group is the largest economic or operational concentration in the synthetic portfolio. **Business implication:** improvements or failures in this group will have disproportionate influence. **Recommended action:** review the group's process drivers before reallocating resources. **Validation:** reproduce the ranking with holdout months and confirm it persists after controlling for entity and volume mix.",
            f"- **Observation:** outcome rates vary by {schema['group_label'].lower()}. **Evidence:** the top observed group is `{top_outcome[schema['group_col']]}` at {top_outcome['outcome_rate']:.1%}, compared with {overall['outcome_rate']:.1%} overall. **Interpretation:** the difference is an association in synthetic observational data. **Business implication:** the segment merits targeted diagnostic work. **Recommended action:** inspect process, mix, and measurement differences before intervention. **Validation:** predefine comparison groups, check sample sizes, and run a prospective test where feasible.",
            "",
            "## Recommendations",
            "",
            *[f"- {item}" for item in config["recommendations"]],
            "",
            "## Limitations",
            "",
            "- The dataset is synthetic and intentionally simplified. It contains no real people, customers, transactions, patients, contracts, or company results.",
            "- Statistical significance does not establish business importance. Effect sizes, intervals, sample sizes, and operating costs must be evaluated together.",
            "- Group differences can reflect data-generation rules, mix, missingness, or measurement choices. Except for the explicitly randomized experiment project, do not interpret them causally.",
            "- A production decision would require real data governance, metric validation, stakeholder review, and monitoring for drift and unintended impacts.",
            "",
            "## Reproducibility",
            "",
            "Run `python src/generate_data.py` and then `python src/analysis.py` from this project directory. Fixed seeds reproduce the committed synthetic data and all calculated outputs.",
        ]
    )
    (reports / "executive_summary.md").write_text("\n".join(executive) + "\n", encoding="utf-8")

    return {"overall": overall, "method_outputs": method_outputs, "top_impact_group": str(top_impact[schema["group_col"]])}


def run_project(project_dir: str | Path, regenerate: bool = False) -> dict[str, Any]:
    project_path = Path(project_dir).resolve()
    config = load_config(project_path)
    raw_path = project_path / "data" / "raw" / "synthetic_data.csv"
    if regenerate or not raw_path.exists():
        generate_dataset(project_path, config)
    return analyze_project(project_path, config)


def write_manifest(rows: list[dict[str, Any]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
