import pytest

@pytest.fixture
def numbers():
    a = 5
    b = 5
    return [a,b]

def multiply(a, b):
    return a * b

def divide(a, b):
    return a * 1.0 / b

def dikalikan_dua(x):
    return multiply(x, 2)

def test_multiply():
    # perkalian
    assert multiply(5, 5) == 25
