"""Testing the CSV flows"""
import pytest
from calc.calculator import Calculator
from calc.historyMod.history import History


@pytest.fixture
def cleanup_fixture():
    """cleanup fixture"""
    History.clear_history()


def csv_addition_test():
    """csv addition"""

