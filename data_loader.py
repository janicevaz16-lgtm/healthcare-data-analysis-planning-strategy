"""Data loading utilities for the UCI Heart Disease Cleveland dataset."""
from pathlib import Path
from typing import Optional
import pandas as pd

COLUMN_NAMES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
]

UCI_CLEVELAND_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/"
    "processed.cleveland.data"
)

def load_heart_disease(path: Optional[str] = None) -> pd.DataFrame:
    """Load a local dataset or retrieve the UCI Cleveland file."""
    candidates = []
    if path:
        candidates.append(Path(path))
    candidates.extend([
        Path("data/raw/processed.cleveland.data"),
        Path("data/raw/heart.csv"),
    ])

    for candidate in candidates:
        if candidate.exists():
            if candidate.suffix.lower() == ".csv":
                df = pd.read_csv(candidate)
            else:
                df = pd.read_csv(candidate, header=None, names=COLUMN_NAMES)
            return _standardize(df)

    df = pd.read_csv(UCI_CLEVELAND_URL, header=None, names=COLUMN_NAMES)
    return _standardize(df)

def _standardize(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize names and convert UCI missing-value markers."""
    df = df.copy()
    df.columns = [str(c).strip().lower() for c in df.columns]
    if "num" in df.columns and "target" not in df.columns:
        df = df.rename(columns={"num": "target"})
    df = df.replace("?", pd.NA)

    for col in ["age", "trestbps", "chol", "thalach", "oldpeak"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df
