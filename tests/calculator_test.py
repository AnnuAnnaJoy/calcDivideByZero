"""Testing the Calculator"""
from calculator.main import Calculator


def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0


def test_calculator_add():
    """Testing the Add function of the calculator"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    # Act by calling the method to be tested
    calc.add_number(4, 5)
    # Assert that the results are correct
    assert calc.result == 9


def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    calc.add_number(1, 2)
    assert calc.get_result() == 3


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(10, 6)
    assert calc.get_result() == 4


def test_calculator_multiplication():
    """ testing multiplication"""
    calc = Calculator()
    calc.multiply_numbers(1, 2)
    assert calc.get_result() == 2


def test_calculator_division():
    """ testing division"""
    calc = Calculator()
    calc.divide_numbers(12, 2)
    assert calc.get_result() == 6
    calc.divide_numbers(1, 0)
    assert calc.get_result() == 0
