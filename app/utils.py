import joblib
import os
from pathlib import Path

def load_model(file_name):
    """
    Charge le modèle Machine Learning depuis le dossier /model.
    Retourne le modèle chargé ou raise en cas d'erreur.
    """
    project_root = Path(__file__).resolve().parent.parent
    model_path = str(project_root) + "/model/" + file_name

    try:
        model = joblib.load(model_path)
        return model

    except Exception as e:
        raise ValueError(f"model_path: {model_path}\nproject_root:{project_root}\n{e}")
        