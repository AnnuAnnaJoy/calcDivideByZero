"""Testing Multiplication"""
from calc.calculation.multiplication import Multiplication


def test_multiplication():
    nos = (5, 2)
    multiplication = Multiplication(nos)
    assert multiplication.get_result() == 10
