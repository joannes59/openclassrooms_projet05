# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from app import utils

# -----------------------------------------------------
# Chargement des encoder et scaler
# -----------------------------------------------------
encoder = utils.load_model("onehotencoder.joblib")
scaler = utils.load_model("scaler.joblib")


def encode(data):
    """ Adapte les données avant la modélisation

    data : instance de InputData model pydantic
    
    """

    # On construit une DataFrame avec une seule ligne
    data_dict = data.model_dump()
    df = pd.DataFrame([data_dict])
    
    # Catégorisation des colonnes, le type permet de les classer en numérique ou en catégorie
    index_columns = ['id_employee']
    target_columns = ['a_quitte_l_entreprise']
    categorical_columns = df.select_dtypes(include='object').columns.tolist()
    numerical_columns = list(set(df.columns) - set(categorical_columns))
    
    # Créer un DataFrame avec les colonnes catégories nominales encodées
    X_encoded_data = encoder.transform(df[categorical_columns])
    X_encoded_data_df = pd.DataFrame(X_encoded_data, columns=encoder.get_feature_names_out(categorical_columns),
                                      index=df.index)
    
    # Ajouter les catégories nominales encodées au dataframe
    X_df = pd.merge(df, X_encoded_data_df, left_index=True, right_index=True, how='inner')
    X_df = X_df.drop(columns=categorical_columns)
    
    # transformation mise a l'échelle
    X_scaled_data = scaler.transform(X_df)
    X_scaled = pd.DataFrame(X_scaled_data, columns=X_df.columns)
    
    return X_scaled

