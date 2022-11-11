import sys
import pytest
# from tests.tests_app import dikalikan_dua, dibagi_dua, add
from tests.tests_app import *


# from tests import add


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


def main():
    num = int(input("masukan angka: "))
    print("kelipatan dari %d adalah %d" % (num, dikalikan_dua(num)))
    print("setengah dari %d adalah %d" % (num, dibagi_dua(num)))
    sys.exit(0)


if __name__ == "__main__":
    main()
