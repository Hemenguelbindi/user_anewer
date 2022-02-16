from pytest import fixture
from fastapi.testclient import TestClient
from main import app


@fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client