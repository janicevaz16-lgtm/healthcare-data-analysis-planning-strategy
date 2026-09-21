"""Classification model construction and evaluation."""
from typing import Dict, Tuple
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score, confusion_matrix
)

def build_models(preprocessor) -> Dict[str, Pipeline]:
    """Return baseline and candidate classification pipelines."""
    return {
        "Majority Baseline": Pipeline([
            ("preprocess", preprocessor),
            ("model", DummyClassifier(strategy="most_frequent")),
        ]),
        "Logistic Regression": Pipeline([
            ("preprocess", preprocessor),
            ("model", LogisticRegression(max_iter=2000, random_state=42)),
        ]),
        "Decision Tree": Pipeline([
            ("preprocess", preprocessor),
            ("model", DecisionTreeClassifier(max_depth=5, random_state=42)),
        ]),
        "Random Forest": Pipeline([
            ("preprocess", preprocessor),
            ("model", RandomForestClassifier(
                n_estimators=300, random_state=42, class_weight="balanced"
            )),
        ]),
    }

def evaluate_models(models, X_train, X_test, y_train, y_test) -> Tuple[pd.DataFrame, Dict]:
    """Fit models and calculate reproducible test-set metrics."""
    rows, fitted = [], {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        fitted[name] = model

        pred = model.predict(X_test)
        score = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else pred

        tn, fp, fn, tp = confusion_matrix(
            y_test, pred, labels=[0, 1]
        ).ravel()

        rows.append({
            "Model": name,
            "Accuracy": accuracy_score(y_test, pred),
            "Precision": precision_score(y_test, pred, zero_division=0),
            "Recall": recall_score(y_test, pred, zero_division=0),
            "F1": f1_score(y_test, pred, zero_division=0),
            "Specificity": tn / (tn + fp) if (tn + fp) else 0,
            "ROC_AUC": roc_auc_score(y_test, score),
            "PR_AUC": average_precision_score(y_test, score),
            "TN": tn, "FP": fp, "FN": fn, "TP": tp,
        })

    return pd.DataFrame(rows), fitted
