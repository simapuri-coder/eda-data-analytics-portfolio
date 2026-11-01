from __future__ import annotations
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
