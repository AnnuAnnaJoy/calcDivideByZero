"""Testing the Calculator"""
from calculator.main import Calculator


def test_calculator_add():
    """Testing the Add function of the calculator"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    assert calc.add_number(4, 5) == 9


def test_calculator_get_result():
    """Testing the add method of the calculator"""
    calc = Calculator()
    assert calc.add_number(1, 2) == 3


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    assert calc.subtract_number(10, 6) == 4


def test_calculator_multiplication():
    """ testing multiplication"""
    calc = Calculator()
    assert calc.multiply_numbers(1, 2) == 2


def test_calculator_division():
    """ testing division"""
    calc = Calculator()
    assert calc.divide_numbers(12, 2) == 6


def zero_division_test(self):
    """ testing division with zero"""
    calc = Calculator()
    with self.assertRaises(ZeroDivisionError):
        calc.divide_numbers(4, 0)
