# -*- coding: utf-8 -*-


from app import utils
from app import schemas
from app import preprocess
import pytest
import json



@pytest.fixture
def data_example():
    """ return data example for input """

    with open("tests/input_data.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        
    data = schemas.InputData(**data_dict)
    return data

def test_encode(data_example):
    """ check the response of encode data """
    x_exemple_scaled = preprocess.encode(data_example)
        

    