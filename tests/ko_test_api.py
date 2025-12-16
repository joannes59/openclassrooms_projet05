# -*- coding: utf-8 -*-

from fastapi.testclient import TestClient
from app import main

client = TestClient(main.app)

def test_predict_endpoint():
    response = client.post(
        "/"
    )

    assert response.status_code == 200
    #assert "prediction" in response.json()

