import csv
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
