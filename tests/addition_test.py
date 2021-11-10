"""Testing Addition"""
from calc.calculation.addition import Addition


def test_addition():
    """testing that our calculator has a static method for addition"""

    nos = (1.0, 2.0)
    addition = Addition.convert_args_to_tuple_of_float(nos)
    assert addition.get_result() == 3
