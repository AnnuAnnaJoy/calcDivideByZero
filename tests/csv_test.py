"""Testing the CSV flows"""
import os

from calc.calculation.csvcalculation import CsvCalc
from calc.utils.csvmanager import CsvManager


def test_read_csv(read_csv_fixture):
    tuple_values = ()
    for index, row in read_csv_fixture.iterrows():
        tuple_values = (row.value1, row.value2)
    assert tuple_values == (14, 11)


def test_csv_process_add(read_csv_fixture):
    df = CsvCalc.csvprocess(read_csv_fixture, 1)
    assert df.loc[1, 'result'] == 3


def test_csv_process_mul(read_csv_fixture):
    df = CsvCalc.csvprocess(read_csv_fixture, 3)
    assert df.loc[8, 'result'] == 66


def test_csv_process_sub(read_csv_fixture):
    df = CsvCalc.csvprocess(read_csv_fixture, 2)
    assert df.loc[3, 'result'] == 17


def test_csv_process_div(read_csv_fixture):
    df = CsvCalc.csvprocess(read_csv_fixture, 4)
    assert df.loc[1, 'result'] == 0.5


def test_add_result_file(read_csv_fixture):
    df = CsvCalc.csvprocess(read_csv_fixture, 1)
    CsvManager.write_csv(df, "addtest")
    base_dir = os.path.dirname(os.getcwd())
    file_path = os.path.join(base_dir, "csv/calc/utils/resultFile")
    os.chdir(file_path)
    print(file_path)
    assert os.path.exists('./addtest_result.csv') is True
