import joblib
import os
from pathlib import Path

def load_model(file_name):
    """
    Charge le modèle Machine Learning depuis le dossier /model.
    Retourne le modèle chargé ou raise en cas d'erreur.
    """
    project_root = '?'

    if os.path.exists('model/' + file_name):
        model_path = 'model/' + file_name
    else:        
        project_root = Path.cwd()
        model_path = os.path.join(project_root, "model", file_name)

    try:
        model = joblib.load(model_path)
        return model

    except Exception as e:
        raise ValueError(f"model_path: {model_path}\n{e}")
        