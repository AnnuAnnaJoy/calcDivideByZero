"""Testing Addition"""
from calc.calculation.addition import Addition


def test_addition():
    """testing that our calculator has a static method for addition"""

    nos = (1, 2)
    addition = Addition(nos)
    assert addition.get_result() == 3
