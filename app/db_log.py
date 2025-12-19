# -*- coding: utf-8 -*-
"""
@author: joannes
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func


# createuser --createdb --username postgres --no-createrole --pwprompt openclassrooms
# createdb -O openclassrooms openclassrooms
DATABASE_URL = "postgresql+psycopg2://openclassrooms:openclassrooms@localhost:5432/openclassrooms"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

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
    
    
def test_connection(engine):
    try:
        with engine.connect() as conn:
            return True
    except:
        return False
    
    
def log_input_data(input_data):
    
    db_input_id = None
    
    if test_connection(engine):
        
        db = SessionLocal()
        db_obj = DBInputData(**input_data.model_dump())
        
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        db_input_id = db_obj.id

    return db_input_id

def log_output_data(output_data: dict):
    
    db_output_id = None
    
    
    if test_connection(engine):
        
        db = SessionLocal()
        db_obj = DBOutputData(**output_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        db_output_id = db_obj.id

    return db_output_id


Base.metadata.create_all(bind=engine)