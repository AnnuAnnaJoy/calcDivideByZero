"""Testing Multiplication"""
from calc.calculation.multiplication import Multiplication


def test_multiplication():
    """testing that our calculator has a static method for addition"""
    nos = (5.0, 2.0)
    multiplication = Multiplication(nos)
    assert multiplication.get_result() == 10
