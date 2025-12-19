from fastapi import FastAPI

from app import schemas
from app import prediction

# -----------------------------------------------------
# Initialisation de l'application
# Local test: 
# export DATABASE_URL="postgresql+psycopg2://openclassrooms:openclassrooms@localhost:5432/openclassrooms"
# uvicorn app.main:app --host 0.0.0.0 --port 7860
# -----------------------------------------------------
app = FastAPI(
    title="API Machine Learning - Openclassrooms Projet 05",
    description="API FastAPI exposant un modèle RandomForest entraîné avec scikit-learn.",
    version="1.0.0"
)

# -----------------------------------------------------
# Définition du schéma d'entrée
# -----------------------------------------------------
InputData = schemas.InputData


# -----------------------------------------------------
# Routes API
# -----------------------------------------------------

@app.get("/")
def home():
    """ Welcome message """
    return prediction.home()

@app.post("/predict")
def predict(data: InputData):
    """ 
    
    return :  {"prediction": integer, 
               "probabilite": float
               }
    """
    return prediction.predict(data)
