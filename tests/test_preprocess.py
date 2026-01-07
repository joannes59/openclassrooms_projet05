# -*- coding: utf-8 -*-


from app import utils
from app import schemas
from app import preprocess
import pytest
import json


def test_load_encoder():
    """ check the configuration model load """
    encoder = utils.load_model("onehotencoder.joblib")
    scaler = utils.load_model("scaler.joblib")
    model = utils.load_model("model.joblib")

    assert encoder is not None
    assert scaler is not None
    assert model is not None


@pytest.fixture
def data_example():
    """ return data example for input """

    with open("tests/input_data.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        
    data = schemas.InputData(**data_dict)
    return data

def test_encode(data_example):
    """ check the response of encode data """
        
    encoder = utils.load_model("onehotencoder.joblib")
    scaler = utils.load_model("scaler.joblib")
    model = utils.load_model("model.joblib")

    if encoder and scaler and model:
        x_exemple_scaled = preprocess.encode(data_example)
        
        if x_exemple_scaled.shape[1] != model.n_features_in_:
            raise ValueError("Incorrect number of features in preprocess")

    