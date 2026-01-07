import joblib
import os

def load_model(file_name):
    """
    Charge le modèle Machine Learning depuis le dossier /model.
    Retourne le modèle chargé ou None en cas d'erreur.
    """

    model_path = os.path.join(
        "model",
        file_name
    )

    try:
        model = joblib.load(model_path)
        return model

    except Exception as e:
        return None
    