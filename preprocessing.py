"""Leakage-aware preprocessing utilities."""
from typing import Tuple
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

TARGET_COLUMN = "target"

def make_train_test_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """Create features and binary target: 0=no disease, 1=disease."""
    data = df.copy()
    if TARGET_COLUMN not in data.columns:
        raise ValueError("Expected a 'target' column.")

    data[TARGET_COLUMN] = pd.to_numeric(data[TARGET_COLUMN], errors="coerce")
    data = data.dropna(subset=[TARGET_COLUMN])

    y = (data[TARGET_COLUMN] > 0).astype(int)
    X = data.drop(columns=[TARGET_COLUMN])
    return X, y

def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    """Build numeric and categorical preprocessing pipelines."""
    categorical = X.select_dtypes(include=["object", "category"]).columns.tolist()
    numeric = X.select_dtypes(include=["number"]).columns.tolist()

    numeric_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    categorical_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    return ColumnTransformer([
        ("numeric", numeric_pipe, numeric),
        ("categorical", categorical_pipe, categorical),
    ])
