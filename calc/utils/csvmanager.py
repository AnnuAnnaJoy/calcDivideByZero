"""CSV Manager"""
import os
import pandas as pd


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
    def write_csv(dataf, operation):
        """ Write to CSV method"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "resultFile")
        file_name = operation + "_result.csv"
        file_loc = os.path.join(file_path, file_name)
        dataf[1:len(dataf) + 1].to_csv(file_loc, index_label='sno')

    @staticmethod
    def path_file():
        """ returns path of csv file method"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "inputFile")
        return file_path
