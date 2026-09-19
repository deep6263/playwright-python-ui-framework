import os
import json
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"

load_dotenv(PROJECT_ROOT / ".env")

class Config:
    def __init__(self):
        self._environment = os.getenv("TEST_ENV", "qa").lower()
        self._config = self._load_config()

    def _load_config(self) -> dict:
        config_file = CONFIG_DIR / f"{self._environment}.json"

        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file '{config_file}' not found.")

        with open(config_file, encoding="utf-8") as file:
            return json.load(file)

    @property
    def base_url(self) -> str:
            return self._config["baseUrl"]

    @property
    def environment(self) -> str:
            return self._config["environment"]
            
            

config = Config()