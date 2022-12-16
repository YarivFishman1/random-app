import pytest
from fastapi.testclient import TestClient
from app.app import app


client = TestClient(app)


@pytest.mark.parametrize('numbers', [
    [3, 2, 1],
    [12, 5, 3, 80, 19],
])
def test_factorial_sainty(numbers):
    numbers_param = '&'.join([f'numbers={number}' for number in numbers])
    numbers.sort()
    response = client.get(f'/sort?{numbers_param}')
    assert response.status_code == 200
    assert response.json() == numbers
