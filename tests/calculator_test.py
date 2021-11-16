"""Testing the Calculator"""
import pprint
import pytest

from calculator.calculator import Calculator
from history.historycalc import History


@pytest.fixture
def setup_cleanup_fixture():
    """cleanup fixture"""
    History.clear_history()


def test_calculator_add(setup_cleanup_fixture):
    """Testing the Add function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert History.history_count() == 4
    assert History.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)


def test_clear_history(setup_cleanup_fixture):
    """test clear history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert History.history_count() == 4
    assert History.clear_history() is True
    assert History.history_count() == 0


def test_count_history(setup_cleanup_fixture):
    """test_count_history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert History.history_count() == 2


def test_get_last_calculation_result(setup_cleanup_fixture):
    """test_get_last_calculation_result"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert History.get_result_of_last_calculation_added_to_history() == 5


def test_get_first_calculation_result(setup_cleanup_fixture):
    """test_get_first_calculation_result"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert History.get_result_of_first_calculation_added_to_history() == 4


def test_calculator_subtract(setup_cleanup_fixture):
    """Testing the subtract method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_number(1, 2) == -1


def test_calculator_multiply(setup_cleanup_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1, 2) == 2


def test_calculator_addition(setup_cleanup_fixture):
    """Testing the Add function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(4, 5) == 9


def test_calculator_get_result(setup_cleanup_fixture):
    # pylint: disable=unused-argument,redefined-outer-name
    """Testing the add method of the calculator"""

    assert Calculator.add_number(1, 2) == 3


def test_calculator_subtraction(setup_cleanup_fixture):
    """Testing the subtract method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_number(10, 6) == 4


def test_calculator_multiplication(setup_cleanup_fixture):
    """ testing multiplication"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1, 2) == 2


def test_calculator_division(setup_cleanup_fixture):
    """ testing division"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(12, 2) == 6
