from pathlib import Path
import sys

PROJECT_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))
from portfolio_core import run_project

if __name__ == "__main__":
    run_project(PROJECT_DIR, regenerate=True)
    print(f"Generated {PROJECT_DIR / 'data/raw/synthetic_data.csv'}")
