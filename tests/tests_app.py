import pytest
from main import *

@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]

def dikalikan_dua(x):
    return multiply(x, 2)

def dibagi_dua(x):
    return divide(x, 2)

class TestApp:
    def test_multiplication(self, numbers):
        res = dikalikan_dua(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = dibagi_dua(numbers[1])
        assert res == numbers[0]
