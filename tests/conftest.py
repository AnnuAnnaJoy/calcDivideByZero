"""Global fixtures"""
import pytest

from calc.calculation.addition import Addition
from calc.calculation.csvcalculation import CsvCalc
from calc.historymod.history import History
from calc.utils.csvmanager import CsvManager


@pytest.fixture
def setup_cleanup_fixture():
    """cleanup fixture"""
    History.clear_history()


@pytest.fixture
def setup_add_number_fixture():
    """add number fixture"""
    values = (1, 2)
    addition = Addition(values)
    History.add_calculation(addition)


@pytest.fixture
def read_csv_fixture():
    """read csv"""
    csvm = CsvManager()
    dataf = csvm.read_csv()
    return dataf


@pytest.fixture
def write_csv_fixture(read_csv_fixture):
    # pylint: disable=unused-argument,redefined-outer-name
    """write csv"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 1)
    CsvManager.write_csv(dataf, "addtest")
