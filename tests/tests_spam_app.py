import mainfunction as min
from mainfunction import numbers

class TestApp:
    def test_kali(self, numbers):
        res = min.dikalikan_dua(numbers[0])
        assert res == numbers[1]

    def test_bagi(self, numbers):
        res = min.dibagi_dua(numbers[1])
        assert res == numbers[0]
