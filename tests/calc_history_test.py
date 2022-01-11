"""Testing the Calculator History"""
from calc.calculation.addition import Addition
from calc.historymod.history import History


def test_clear_history(setup_cleanup_fixture, setup_add_number_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.history_count() == 1
    assert History.clear_history() is True
    assert History.history_count() == 0


def test_count_history(setup_cleanup_fixture, setup_add_number_fixture):
    """testing history count"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.history_count() == 1
    values = (5, 10)
    History.add_calculation(Addition(values))
    assert History.history_count() == 2


def test_get_calculation(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_calculation(0).get_result() == 3


def test_get_calc_last_result_value(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_last_calculation_result_value() == 3


def test_get_calculation_first(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_first_calculation().get_result() == 3


def test_get_calc_last_result_object(setup_cleanup_fixture, setup_add_number_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert isinstance(History.get_last_calculation_object(), Addition)
