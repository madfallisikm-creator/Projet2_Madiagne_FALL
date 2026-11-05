"""Prédiction : charge models/model.joblib et prédit 0 (normal) ou 1 (attaque)."""
from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "model.joblib"
_model = None


def predict(df: pd.DataFrame) -> list:
    """df : mêmes colonnes que flux_train.csv, SANS 'attaque'.
    Retourne une liste de 0 (normal) ou 1 (attaque), une valeur par ligne."""
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return [int(p) for p in _model.predict(df)]
