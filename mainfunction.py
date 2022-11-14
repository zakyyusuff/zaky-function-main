import pytest

@pytest.mark.parametrize("a, b, c", [(10,20, 30), (20,40,60), (11,22,33)])
def test_add(a, b, c):
    res = add(a, b)
    assert res == c

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a * 1.0 / b

@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]

def dikalikan_dua(x):
    return multiply(x, 2)

def dibagi_dua(x):
    return divide(x, 2)

@pytest.mark.easy_operation
def test_add():
    # penjumlahan
    assert add(4, 8) == 12

@pytest.mark.easy_operation
def test_subtract():
    # pengurangan
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    # perkalian
    assert multiply(5, 5) == 25

@pytest.mark.difficult_operation
def test_divide():
    # pembagian
    assert divide(21, 3) == 7

