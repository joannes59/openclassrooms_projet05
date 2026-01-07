from typing import Literal
from pydantic import BaseModel, Field


class InputData(BaseModel):
    """Définition des données d'entrée décrivant 
    le profil professionnel et personnel d'un employé."""

    id_employee: int = Field(
        ...,
        description="Identifiant unique de l'employé dans le système d'information RH"
    )

    age: int = Field(
        ...,
        ge=16,
        le=70,
        description="Âge de l'employé exprimé en années"
    )

    statut_marital: Literal['Célibataire', 'Divorcé(e)', 'Marié(e)'] = Field(
        ...,
        description="Situation matrimoniale actuelle de l'employé"
    )

    poste: Literal[
        'Assistant de Direction',
        'Cadre Commercial',
        'Consultant',
        'Directeur Technique',
        'Manager',
        'Représentant Commercial',
        'Ressources Humaines',
        'Senior Manager',
        'Tech Lead'
    ] = Field(
        ...,
        description="Intitulé du poste occupé actuellement par l'employé"
    )

    nombre_experiences_precedentes: int = Field(
        ...,
        ge=0,
        le=20,
        description="Nombre total d'expériences professionnelles précédentes avant le poste actuel"
    )

    annee_experience_totale: int = Field(
        ...,
        ge=0,
        le=65,
        description="Nombre total d'années d'expérience professionnelle cumulée"
    )

    annees_dans_le_poste_actuel: int = Field(
        ...,
        ge=0,
        le=65,
        description="Ancienneté de l'employé dans son poste actuel, exprimée en années"
    )

    satisfaction_employee_environnement: int = Field(
        ...,
        ge=1,
        le=4,
        description="Niveau de satisfaction de l'employé concernant son environnement de travail (1 = très insatisfait, 4 = très satisfait)"
    )

    note_evaluation_precedente: int = Field(
        ...,
        ge=1,
        le=4,
        description="Note obtenue lors de la dernière évaluation annuelle de performance"
    )

    niveau_hierarchique_poste: int = Field(
        ...,
        ge=1,
        le=5,
        description="Niveau hiérarchique associé au poste occupé (1 = niveau opérationnel, 5 = direction)"
    )

    satisfaction_employee_nature_travail: int = Field(
        ...,
        ge=1,
        le=4,
        description="Niveau de satisfaction de l'employé concernant la nature de ses missions"
    )

    satisfaction_employee_equipe: int = Field(
        ...,
        ge=1,
        le=4,
        description="Niveau de satisfaction de l'employé vis-à-vis de son équipe de travail"
    )

    satisfaction_employee_equilibre_pro_perso: int = Field(
        ...,
        ge=1,
        le=4,
        description="Niveau de satisfaction concernant l'équilibre entre vie professionnelle et vie personnelle"
    )

    heure_supplementaires: Literal['Non', 'Oui'] = Field(
        ...,
        description="Indique si l'employé effectue régulièrement des heures supplémentaires"
    )

    augmentation_salaire: int = Field(
        ...,
        ge=0,
        description="Pourcentage d'augmentation du salaire de l'employé"
    )

    nombre_participation_pee: int = Field(
        ...,
        ge=0,
        description="Nombre de participations de l'employé à un plan d'épargne entreprise (PEE)"
    )

    nb_formations_suivies: int = Field(
        ...,
        ge=0,
        description="Nombre total de formations professionnelles suivies par l'employé"
    )

    distance_domicile_travail: int = Field(
        ...,
        ge=0,
        description="Distance entre le domicile de l'employé et son lieu de travail (en kilomètres)"
    )

    niveau_education: int = Field(
        ...,
        ge=1,
        le=5,
        description="Niveau d'éducation de l'employé (1 = niveau le plus bas, 5 = niveau le plus élevé)"
    )

    domaine_etude: Literal[
        'Autre',
        'Entrepreunariat',
        'Infra & Cloud',
        'Marketing',
        'Ressources Humaines',
        'Transformation Digitale'
    ] = Field(
        ...,
        description="Domaine principal d'activités de l'employé"
    )

    frequence_deplacement: Literal['Aucun', 'Frequent', 'Occasionnel'] = Field(
        ...,
        description="Fréquence des déplacements professionnels liés au poste"
    )

    annees_depuis_la_derniere_promotion: int = Field(
        ...,
        ge=0,
        le=25,
        description="Nombre d'années écoulées depuis la dernière promotion de l'employé"
    )

    annes_sous_responsable_actuel: int = Field(
        ...,
        ge=0,
        le=25,
        description="Nombre d'années pendant lesquelles l'employé travaille sous son responsable hiérarchique actuel"
    )
