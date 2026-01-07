import joblib
import os

def load_model(file_name):
    """
    Charge le modèle Machine Learning depuis le dossier /model.
    Retourne le modèle chargé ou None en cas d'erreur.
    """
    docker_root = '/code'
    if os.path.exists(docker_root):
        root_code = docker_root
    else:
        root_code = os.path.dirname(__file__) + '/..'
        
    model_path = os.path.join(root_code, "model", file_name)

    try:
        model = joblib.load(model_path)
        return model

    except Exception as e:
        return None
    