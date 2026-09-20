from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "dataset.csv"

MODEL_DIR = BASE_DIR / "models"
RESULTS_DIR = BASE_DIR / "results"

MODEL_PATH = MODEL_DIR / "xgboost_pcos_model.pkl"

TARGET_COLUMN = "PCOS"

TEST_SIZE = 0.20
RANDOM_STATE = 42