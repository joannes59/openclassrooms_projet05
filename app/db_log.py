# -*- coding: utf-8 -*-
"""
@author: joannes
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func
import os


# createuser --createdb --username postgres --no-createrole --pwprompt openclassrooms
# createdb -O openclassrooms openclassrooms
# EXPORT DATABASE_URL="postgresql+psycopg2://openclassrooms:openclassrooms@localhost:5432/openclassrooms"

# Récupération de la variable d'envirronnement de connection à la base de donnée
DATABASE_URL = os.getenv("DATABASE_URL")


# -----------------------------------------------------
# Vérification de la connection à la base de données
# la base de donnée n'est pas disponible sur HuggingFace
# -----------------------------------------------------
engine = None
DBsession = None

if DATABASE_URL:
    try:
        engine = create_engine(DATABASE_URL, echo=False)
        DBsession = sessionmaker(bind=engine)
        print(f"Base de données: \n {DATABASE_URL}")
    except Exception as e:
        print(f"Base de données indisponible : {e}")

def test_connection(engine):
    """ Check the connection to db """
    if not engine:
        return False
    
    try:
        with engine.connect() as conn:
            return True
    except:
        return False


# -----------------------------------------------------
# Définition des tables
# -----------------------------------------------------

Base = declarative_base()

class DBInputData(Base):
    __tablename__ = "db_input_data"

    id = Column(Integer, primary_key=True, index=True)

    id_employee = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    statut_marital = Column(String(50))
    poste = Column(String(100))

    nombre_experiences_precedentes = Column(Integer)
    annee_experience_totale = Column(Integer)
    annees_dans_le_poste_actuel = Column(Integer)

    satisfaction_employee_environnement = Column(Integer)
    note_evaluation_precedente = Column(Integer)
    niveau_hierarchique_poste = Column(Integer)
    satisfaction_employee_nature_travail = Column(Integer)
    satisfaction_employee_equipe = Column(Integer)
    satisfaction_employee_equilibre_pro_perso = Column(Integer)

    heure_supplementaires = Column(String(10))

    augmentation_salaire = Column(Integer)
    nombre_participation_pee = Column(Integer)
    nb_formations_suivies = Column(Integer)
    distance_domicile_travail = Column(Integer)

    niveau_education = Column(Integer)
    domaine_etude = Column(String(100))
    frequence_deplacement = Column(String(50))

    annees_depuis_la_derniere_promotion = Column(Integer)
    annes_sous_responsable_actuel = Column(Integer)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class DBOutputData(Base):
    __tablename__ = "db_output_data"

    id = Column(Integer, primary_key=True, index=True)

    id_input_data = Column(Integer, nullable=False)
    prediction =  Column(Integer)
    probabilite =  Column(Float)
    
    
# -----------------------------------------------------
# Création des tables
# -----------------------------------------------------
if test_connection(engine):
    Base.metadata.create_all(bind=engine)
    
    
# -----------------------------------------------------
# Fonctions d'enregistrement des log
# -----------------------------------------------------
    
def log_input_data(input_data):
    """ Enregistrement des données d'entrée au format pydantic """
    
    db_input_id = None
    
    if test_connection(engine):
        
        db = DBsession()
        db_obj = DBInputData(**input_data.model_dump())
        
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        db_input_id = db_obj.id

    return db_input_id

def log_output_data(output_data: dict):
    """ Enregistrement des données de sortie au format dictionnaire """
    
    db_output_id = None
    
    
    if test_connection(engine):
        
        db = DBsession()
        db_obj = DBOutputData(**output_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        db_output_id = db_obj.id

    return db_output_id

