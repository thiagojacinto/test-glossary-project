import pytest
from fastapi.testclient import TestClient

from testglossary.main import app, active_API_version

client = TestClient(app)
active_target_url = '/api/{}/healthcheck'.format(active_API_version)

def test_active_API_version_should_be_a_string():
    "validate if active_API_version is a string"
    assert isinstance(active_API_version, str)

def test_should_return_status_as_OK():
    response = client.get(active_target_url)
    assert response.status_code == 200
    assert response.json() == { "status": "OK" }

def test_should_return_status_as_not_None():
    response = client.get(active_target_url)
    assert response.json() is not None

def test_should_return_status_code_200():
    response = client.get(active_target_url)
    assert response.status_code == 200