# -*- coding: utf-8 -*-
"""
@author: joannes
"""

import joblib
import os
import numpy as np
from app import prediction
from app import utils
from app import schemas
import pytest
import json

model_files = ['model/model.joblib', 'model/onehotencoder.joblib', 'model/scaler.joblib']
model = utils.load_model("model.joblib")


def test_load_model():
    """ Check if model files exist """
    for file_name in model_files:
        assert os.path.exists(file_name)
        
    model = utils.load_model("model.joblib")
        
    assert model is not None
        
        
@pytest.fixture
def data_example():
    """ return data example for input """

    with open("tests/input_data.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        
    data = schemas.InputData(**data_dict)
    return data

def test_predict(data_example):
    """ Check reponse of prediction """
    prediction.predict(data_example)
    
    
