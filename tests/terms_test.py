import pytest
from fastapi.testclient import TestClient

from testglossary.main import app, active_API_version

client = TestClient(app)
active_target_url = '/api/{}/terms'.format(active_API_version)

def test_should_return_an_array():
    response = client.get(active_target_url)
    assert response.status_code == 200
    assert isinstance(response.json(), list) == True


def test_should_return_status_code_200():
    response = client.get(active_target_url)
    assert response.status_code == 200


def test_should_return_404_on_not_found_resource():
    response = client.get('{}/2'.format(active_target_url))
    assert response.status_code == 404
