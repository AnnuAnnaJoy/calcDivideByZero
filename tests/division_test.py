"""Testing Division"""
from calc.calculation.division import Division


def test_division():
    """testing division class"""
    nos = (10.0, 2.0)
    division = Division(nos)
    assert division.get_result() == 0.05
