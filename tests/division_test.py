"""Testing Division"""
from calc.calculation.division import Division


def test_division():
    nos = (10, 2)
    division = Division(nos)
    assert division.get_result() == 5


def test_divisionbyzero(self):
    no1 = (10, 0)
    with self.assertRaises(ZeroDivisionError):
        Division(no1).get_result()
