import pandas as pd
import os


class CsvManager:

    def read_csv(self):
        """ Read CSV method"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "inputFile")
        file_loc = os.path.join(file_path, "smallset.csv")
        if os.listdir(file_path):
            df = pd.read_csv(file_loc, dtype={"sno": int, "value1": int, "value2": int})
            df.set_index('sno', inplace=True)
        return df

    @staticmethod
    def write_csv(df, operation):
        """ Write to CSV method"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "resultFile")
        file_name = operation + "_result.csv"
        file_loc = os.path.join(file_path, file_name)
        df[1:len(df) + 1].to_csv(file_loc, index_label='sno')
