import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_home_endpoint(client, monkeypatch):
    # Mock de prediction.home
    def mock_home():
        return {"message": "API opérationnelle"}

    monkeypatch.setattr(
        "app.main.prediction.home",
        mock_home
    )

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API opérationnelle"}
