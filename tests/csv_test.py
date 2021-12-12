"""Testing the CSV flows"""
import os
import logging

from calc.calculation.csvcalculation import CsvCalc
from calc.utils.csvmanager import CsvManager

logging.basicConfig(
    filename='result_logs/app.log', filemode='w', level=logging.NOTSET,
    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def test_read_csv(read_csv_fixture):
    """test_read_csv"""
    tuplevalues = ()
    for index, row in read_csv_fixture.iterrows():
        tuplevalues = (row.value1, row.value2)
        logger.debug("As per file %s %s  - %s , %s = %s", os.listdir(CsvManager.path_file()), index,
                     row.value1, row.value2, tuplevalues)
    assert tuplevalues == (5, 0)


def test_csv_process_add(read_csv_fixture):
    """test_csv_process_add"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 1)
    logger.debug(
        "As per file %s %s  - %s + %s = %s", os.listdir(CsvManager.path_file()), dataf.index[1],
        dataf.loc[1, 'value1'], dataf.loc[1, 'value2'], dataf.loc[1, 'result'])
    assert dataf.loc[1, 'result'] == 3


def test_csv_process_mul(read_csv_fixture):
    """test_csv_process_mul"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 3)
    logger.debug(
        "As per file %s %s  - %s * %s = %s", os.listdir(CsvManager.path_file()), dataf.index[3],
        dataf.loc[3, 'value1'], dataf.loc[3, 'value2'],
        dataf.loc[3, 'result'])
    assert dataf.loc[3, 'result'] == 38


def test_csv_process_sub(read_csv_fixture):
    """test_csv_process_sub"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 2)
    logger.debug(
        "As per file %s %s  - %s - %s = %s", os.listdir(CsvManager.path_file()), dataf.index[2],
        dataf.loc[2, 'value1'], dataf.loc[2, 'value2'],
        dataf.loc[2, 'result'])
    assert dataf.loc[2, 'result'] == 12


def test_csv_process_div(read_csv_fixture):
    """test_csv_process_div"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 4)
    logger.debug(
        "As per file %s %s  - %s / %s = %s", os.listdir(CsvManager.path_file()), dataf.index[11],
        dataf.loc[11, 'value1'], dataf.loc[11, 'value2'],
        dataf.loc[11, 'result'])
    assert dataf.loc[11, 'result'] == 3


def test_add_result_file(read_csv_fixture):
    """test_add_result_file"""
    dataf = CsvCalc.csvprocess(read_csv_fixture, 1)
    CsvManager.write_csv(dataf, "addtest")
    base_dir = os.path.dirname(os.getcwd())
    file_path = os.path.join(base_dir, "csv/calc/utils/resultFile/")
    os.chdir(file_path)
    print(file_path)
    assert os.path.exists('./addtest_result.csv') is True
