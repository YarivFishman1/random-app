import pytest
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)


@pytest.mark.parametrize('name', ['Ben', 'Dan', 'Bob'])
def test_welcome_sainty(name):
    response = client.get(f'/welcome?name={name}')
    assert response.status_code == 200
    assert response.text == f'"Welcome {name}"'


def test_welcome_no_input():
    response = client.get('/welcome')
    assert response.status_code == 422
