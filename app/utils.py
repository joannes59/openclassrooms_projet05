import joblib
import os
from pathlib import Path

def load_model(file_name):
    """
    Charge le modèle Machine Learning depuis le dossier /model.
    Retourne le modèle chargé ou None en cas d'erreur.
    """

    if os.path.exists('model/' + file_name):
        model_path = 'model/' + file_name
    else:        
        project_root = Path(__file__).resolve().parents[1]
        model_path = os.path.join(project_root, "model", file_name)

    try:
        model = joblib.load(model_path)
        return model

    except Exception as e:
        
        return None
    