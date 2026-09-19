import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

def load_json(file_name: str) -> dict:
    file_path = DATA_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Data file '{file_path}' not found.")

    with open(file_path, encoding="utf-8") as file:
        return json.load(file)