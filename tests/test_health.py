import pytest
from fastapi.testclient import TestClient

from app import server


@pytest.fixture
def client():
    return TestClient(server)


def test_health(client):
    """Test if the api is healthy (/health returns 200)"""
    response = client.get("/health")
    assert response.status_code == 200
