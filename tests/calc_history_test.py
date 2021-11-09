"""Testing the Calculator History"""
import pprint

from calc.calculation.addition import Addition
from calc.calculator import Calculator
from calc.historyMod.history import History

import pytest


@pytest.fixture
def setup_cleanup_fixture():
    History.clear_history()


@pytest.fixture
def setup_add_number_fixture():
    values = (1, 2)
    addition = Addition(values)
    History.add_calculation(addition)


def test_clear_history(setup_cleanup_fixture, setup_add_number_fixture):
    assert History.history_count() == 1
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert History.history_count() == 4
    assert History.clear_history() == True
    assert History.history_count() == 0


def test_count_history(setup_cleanup_fixture, setup_add_number_fixture):
    assert History.history_count() == 1
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert History.history_count() == 3


def test_get_calculation(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_calculation(0).get_result() == 3


def test_get_calc_last_result_value(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing getting the last calculation from the history"""
    assert History.get_last_calculation_result_value() == 3


def test_get_calculation_first(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing getting the last calculation from the history"""
    assert History.get_first_calculation().get_result() == 3


def test_get_calc_last_result_object(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing getting the last calculation from the history"""
    # This test if it returns the last calculation as an object
    assert isinstance(History.get_last_calculation_object(), Addition)
