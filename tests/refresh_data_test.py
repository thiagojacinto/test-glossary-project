import random
import uuid

import pytest
from fastapi.testclient import TestClient

from testglossary.main import active_API_version

endpoint_path = "terms/refresh/"
active_target_url = "/api/{}/{}".format(active_API_version, endpoint_path)


@pytest.fixture()
def generate_random_string(containing: str = None) -> str:
    if containing is None:
        return uuid.uuid4().__str__()

    random_uuid = uuid.uuid4().__str__()
    return containing.rjust(len(random_uuid), random_uuid)


def test_when_register_a_new_term_then_should_return_201(
    test_app: TestClient, generate_random_string
):
    body = {
        "name": generate_random_string,
        "definition": generate_random_string,
        "acronym": "test-subject",
        "version": 0,
        "language_id": 0,
    }
    response = test_app.post(active_target_url, json=body)

    assert response.status_code == 201


def test_when_register_a_new_term_then_should_return_success(
    test_app: TestClient, generate_random_string
):
    body = {
        "name": generate_random_string,
        "definition": generate_random_string,
        "acronym": "test-subject",
        "version": 0,
        "language_id": 0,
    }
    response = test_app.post(active_target_url, json=body)

    assert response.json().get("result") is True
    assert isinstance(response.json().get("id"), int)


def test_when_attempt_to_register_an_invalid_term_then_should_return_error(
    test_app: TestClient, generate_random_string
):
    body = {
        "name": generate_random_string,
        "definition": generate_random_string,
        "acronym": "test-subject-error",
        "version": random.randint(1000, 99999),
        "language_id": random.randint(1000, 99999),
    }
    response = test_app.post(active_target_url, json=body)

    assert response.status_code == 422
    assert response.json().get("detail") is not None
    assert "error" in response.json().get("detail")


def test_when_attempt_to_register_an_incomplete_term_then_should_return_error(
    test_app: TestClient
):
    body = {"acronym": "test-subject-error",
            "language_id": random.randint(1000, 99999)}
    response = test_app.post(active_target_url, json=body)

    assert response.status_code == 422
    assert response.json().get("detail") is not None
    error_list = [
        item for item in response.json().get("detail") if "missing" in item.get("type")
    ]
    assert len(error_list) > 0
