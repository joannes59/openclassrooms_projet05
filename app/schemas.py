from pydantic import BaseModel, Field
from typing import Literal


class InputData(BaseModel):
    """ Définition des entrées du modèle."""
    
    id_employee: int = Field(..., description="Identifiant unique de l'employé")

    age: int = Field(..., ge=16, le=70)

    statut_marital: Literal['Célibataire', 'Divorcé(e)', 'Marié(e)']

    poste: Literal[
        'Assistant de Direction', 'Cadre Commercial', 'Consultant', 'Directeur Technique',
        'Manager', 'Représentant Commercial', 'Ressources Humaines', 'Senior Manager', 'Tech Lead'
    ]

    nombre_experiences_precedentes: int = Field(..., ge=0, le=20)
    annee_experience_totale: int = Field(..., ge=0, le=65)
    annees_dans_le_poste_actuel: int = Field(..., ge=0, le=65)

    satisfaction_employee_environnement: int = Field(..., ge=1, le=4)
    note_evaluation_precedente: int = Field(..., ge=1, le=4)
    niveau_hierarchique_poste: int = Field(..., ge=1, le=5)
    satisfaction_employee_nature_travail: int = Field(..., ge=1, le=4)
    satisfaction_employee_equipe: int = Field(..., ge=1, le=4)
    satisfaction_employee_equilibre_pro_perso: int = Field(..., ge=1, le=4)

    heure_supplementaires: Literal['Non', 'Oui']

    augmentation_salaire: int = Field(..., ge=0)
    nombre_participation_pee: int = Field(..., ge=0)
    nb_formations_suivies: int = Field(..., ge=0)
    distance_domicile_travail: int = Field(..., ge=0)

    niveau_education: int = Field(..., ge=1, le=5)
    
    domaine_etude: Literal['Autre', 'Entrepreunariat', 'Infra & Cloud', 'Marketing',
                           'Ressources Humaines', 'Transformation Digitale']
    
    frequence_deplacement: Literal['Aucun', 'Frequent', 'Occasionnel']
    
    annees_depuis_la_derniere_promotion: int = Field(..., ge=0, le=25)
    annes_sous_responsable_actuel: int = Field(..., ge=0, le=25)
    
    
    