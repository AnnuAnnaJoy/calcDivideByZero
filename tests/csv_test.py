"""Testing the CSV flows"""
import os

from calc.calculation.csvcalculation import CsvCalc
from calc.utils.csvmanager import CsvManager


def test_read_csv(read_csv_fixture):
    """test_read_csv"""
    tuplevalues = ()
    for _, row in read_csv_fixture.iterrows():
        tuplevalues = (row.value1, row.value2)
    assert tuplevalues == (14, 11)


def test_csv_process_add(read_csv_fixture):
    """test_csv_process_add"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 1)
    assert dataf.loc[1, 'result'] == 3


def test_csv_process_mul(read_csv_fixture):
    """test_csv_process_mul"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 3)
    assert dataf.loc[8, 'result'] == 66


def test_csv_process_sub(read_csv_fixture):
    """test_csv_process_sub"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 2)
    assert dataf.loc[3, 'result'] == 17


def test_csv_process_div(read_csv_fixture):
    """test_csv_process_div"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 4)
    assert dataf.loc[1, 'result'] == 0.5


def test_add_result_file(read_csv_fixture):
    """test_add_result_file"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 1)
    CsvManager.write_csv(dataf, "addtest")
    base_dir = os.path.dirname(os.getcwd())
    file_path = os.path.join(base_dir, "csv/calc/utils/resultFile/")
    os.chdir(file_path)
    print(file_path)
    assert os.path.exists('./addtest_result.csv') is True
