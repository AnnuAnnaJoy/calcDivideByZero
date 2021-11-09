"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.historyMod.history import History


@pytest.fixture
def setup_cleanup_fixture():
    History.clear_history()


def test_calculator_add(setup_cleanup_fixture):
    """Testing the Add function of the calculator"""
    # Arrange by instantiating the calc class
    Calculator.add_number(4, 5)
    assert Calculator.get_result_value() == 9


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    Calculator.subtract_number(10, 6)
    assert Calculator.get_result_value() == 4


def test_calculator_multiplication():
    """ testing multiplication"""
    Calculator.multiply_numbers(1, 2)
    assert Calculator.get_result_value() == 2


def test_calculator_division():
    """ testing division"""
    Calculator.divide_numbers(12, 2)
    assert Calculator.get_result_value() == 6


def zero_division_test(self):
    """ testing division with zero"""
    with self.assertRaises(ZeroDivisionError):
        Calculator.divide_numbers(4, 0)
