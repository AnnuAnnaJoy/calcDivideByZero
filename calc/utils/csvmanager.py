"""CSV Manager"""
import os

import pandas as pd
from pandas.io.formats import string


class CsvManager:
    """CSV"""

    @staticmethod
    def read_csv():
        """ Read CSV method"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "inputFile")
        file_loc = os.path.join(file_path, "smallset.csv")
        if os.listdir(file_path):
            dataf = pd.read_csv(file_loc, dtype={"sno": int, "value1": int, "value2": int})
            dataf.set_index('sno', inplace=True)
        return dataf

    @staticmethod
    def read_resultcsv():
        """ Read Result CSV method"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "resultFile")
        file_loc = os.path.join(file_path, "results.csv")
        if os.listdir(file_path):
            dataf = pd.read_csv(file_loc, dtype={"value1": int, "value2": int, "operation": object})
        return dataf

    @staticmethod
    def write_csv(dataf, operation):
        """ Write to CSV method"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "resultFile")
        if operation == '':
            file_name = 'results.csv'
        else:
            file_name = operation + "_result.csv"
        file_loc = os.path.join(file_path, file_name)
        dataf[1:len(dataf) + 1].to_csv(file_loc, index_label='sno')

    @staticmethod
    def write_resultscsv(dframe):
        """ Write to CSV method"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "resultFile")
        file_name = 'results.csv'
        file_loc = os.path.join(file_path, file_name)
        dframe.to_csv(file_loc, index=False, mode='a', header=False)

    @staticmethod
    def path_file():
        """ returns path of csv file method"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "inputFile")
        return file_path

    @staticmethod
    def writecalctocsv(tuple1, columns):
        """writeCalcToCSV"""
        dframe = pd.DataFrame([tuple1], columns=columns)
        dframe.drop_duplicates(inplace=True)
        CsvManager.write_resultscsv(dframe)
