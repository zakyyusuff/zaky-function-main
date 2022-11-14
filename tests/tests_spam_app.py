import mainfunction as min
# import pytest
from mainfunction import numbers

class TestApp:
    # @pytest.mark.easy_operation
    def test_kali(self, numbers):
        res = min.dikalikan_dua(numbers[0])
        assert res == numbers[1]

    # @pytest.mark.easy_operation
    def test_bagi(self, numbers):
        res = min.dibagi_dua(numbers[1])
        assert res == numbers[0]
