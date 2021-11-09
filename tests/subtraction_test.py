"""Testing Subtraction"""
from calc.calculation.subtraction import Subtraction


def test_subtraction():
    nos = (5, 2)
    subtraction = Subtraction(nos)
    assert subtraction.get_result() == 3
