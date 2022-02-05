from pytest import fixture
from starlette.config import environ
from fastapi.testclient import TestClient
from db.test_connector import get_database
from main import app


@fixture(scope="session")
def test_user():
    return {
        "user": {
            "email": "user1@example.com",
            "password": "string1",
            "username": "string1"
        }
    }


@fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@fixture(scope="session")
def test_client(test_user):
    with TestClient(app) as test_client:
        yield test_client

    import asyncio
    asyncio.run(get_database())





environ['TESTING'] = 'TRUE'