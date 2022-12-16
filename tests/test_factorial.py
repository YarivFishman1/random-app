import pytest
from fastapi.testclient import TestClient
from app.app import app

import math

client = TestClient(app)


@pytest.mark.parametrize('number', [3, 4, 5])
def test_factorial_sainty(number):
    response = client.get(f'/factorial?number={number}')
    assert response.status_code == 200
    assert int(response.text) == math.factorial(number)
