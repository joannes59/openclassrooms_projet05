# -*- coding: utf-8 -*-
"""
@author: joannes
"""

import joblib
import os
import numpy as np
from app import schemas
import pytest

model_files = ['model/model.joblib', 'model/onehotencoder.joblib', 'model/scaler.joblib']

@pytest.fixture
def data():
    """ Check if model files exist """
    for file_name in model_files:
        assert os.path.exists(file_name)
        
    input_field = []
    for name, field in schemas.InputData.model_fields.items():
        input_field.append(name)
    #print(name, '------', field.annotation, field.metadata)
    print(input_field)
    

def test_load_model(data):

    model = joblib.load("model/model.joblib")
    print('model: ', set( model.feature_names_in_))

    scaler = joblib.load("model/scaler.joblib")
    print('scaler: ', scaler.feature_names_in_)
    
    
