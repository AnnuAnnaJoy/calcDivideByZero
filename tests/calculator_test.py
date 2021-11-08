"""Testing the Calculator"""
import pprint

from calc.addition import Addition
from calculator.calculator import Calculator
from history.history import History

import pytest


@pytest.fixture
def setup_cleanup_fixture():
    History.clear_history()


@pytest.fixture
def setup_add_number_fixture():
    values = (1, 2)
    addition = Addition(values)
    Calculator.add_number(addition)


def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert History.history_count() == 4
    assert History.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)


def test_clear_history(clear_history):
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert History.history_count() == 4
    assert History.clear_history() == True
    assert History.history_count() == 0


def test_count_history(clear_history):
    assert History.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert History.history_count() == 2


def test_get_last_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5


def test_get_first_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4


def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1


def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 2) == 2


def test_calculator_add(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing the Add function of the calculator"""

    assert Calculator.add_number(4, 5) == 9


def test_calculator_get_result(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing the add method of the calculator"""

    assert Calculator.add_number(1, 2) == 3


def test_calculator_subtract(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing the subtract method of the calculator"""

    assert Calculator.subtract_number(10, 6) == 4


def test_calculator_multiplication(setup_cleanup_fixture, setup_add_number_fixture):
    """ testing multiplication"""

    assert Calculator.multiply_numbers(1, 2) == 2


def test_calculator_division(setup_cleanup_fixture, setup_add_number_fixture):
    """ testing division"""

    assert Calculator.divide_numbers(12, 2) == 6


def zero_division_test(self):
    """ testing division with zero"""

    with self.assertRaises(ZeroDivisionError):
        Calculator.divide_numbers(4, 0)
