from app import preprocess
from app import utils
from app import db_log

# -----------------------------------------------------
# Chargement du modèle
# -----------------------------------------------------
model = utils.load_model("model.joblib")

def home():
    """ message de bienvenue """
    message =  {
        "message": "Bienvenue sur l'API Ressource Humaine",
        "documentation": "/docs",
    }
    return message 

def predict(data):

    if model is None:
        return {"error": "Modèle non chargé"}
    
    # log the data in postgres db
    db_input_id = db_log.log_input_data(data)
    
    # encodage
    X = preprocess.encode(data)

    # Prédiction
    y = model.predict(X)
    y_proba = model.predict_proba(X)
    
    # format reponse
    response = {"prediction": int(y[0]), "probabilite": float(y_proba[0][1])}
    
    # log the response in postgres db
    if db_input_id:
        output_data = response.copy()
        output_data['id_input_data'] = db_input_id
        db_output_id = db_log.log_output_data(output_data)

    return response
