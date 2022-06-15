import pytest
from fastapi.testclient import TestClient

from testglossary.main import app


@pytest.fixture(scope="module")
def test_app():
    """Fixture to handle Test Client"""
    test_client = TestClient(app)
    yield test_client
