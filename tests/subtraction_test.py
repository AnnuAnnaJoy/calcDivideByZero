"""Testing Subtraction"""
from calc.calculation.subtraction import Subtraction


def test_subtraction():
    """testing that our calculator has a static method for subtraction"""
    nos = (5.0, 2.0)
    subtraction = Subtraction(nos)
    assert subtraction.get_result() == 3
