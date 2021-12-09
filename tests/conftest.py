import pytest

from calc.calculation.addition import Addition
from calc.calculation.csvcalculation import CsvCalc
from calc.historyMod.history import History
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
    cv = CsvManager()
    df = cv.read_csv()
    return df


@pytest.fixture
def setup_calculation_fixture():
    df = read_csv_fixture()
    tuple1 = df.value_1[0], df.value_2[0]
    return tuple1


@pytest.fixture
def write_csv_fixture(read_csv_fixture):
    """write csv"""
    df = CsvCalc.csvprocess(read_csv_fixture, 1)
    CsvManager.write_csv(df, "addtest")
