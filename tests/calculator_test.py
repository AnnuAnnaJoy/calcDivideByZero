"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.historyMod.history import History


@pytest.fixture
def setup_cleanup_fixture():
    """cleanup fixture"""
    History.clear_history()


def test_calculator_add(setup_cleanup_fixture):
    """Testing the Add function of the calculator"""
    # Arrange by instantiating the calc class
    my_tuple = (1.0, 2.0, 5.0)
    Calculator.add_number(my_tuple)
    assert Calculator.get_last_result_value() == 8.0


def test_calculator_subtract(setup_cleanup_fixture):
    """Testing the subtract method of the calculator"""
    my_tuple = (1.0, 2.0, 3.0)
    Calculator.subtract_number(my_tuple)
    assert Calculator.get_last_result_value() == -4.0


def test_calculator_multiplication(setup_cleanup_fixture):
    """ testing multiplication"""
    my_tuple = (1.0, 2.0, 3.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 6


def test_calculator_division(setup_cleanup_fixture):
    """ testing division"""
    Calculator.divide_numbers(12, 2)
    assert Calculator.get_last_result_value() == 6
