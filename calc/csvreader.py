import pandas as pd
import os
from calc.calculator import Calculator


class CsvManager:
    if os.listdir(os.getcwd()):
        df = pd.read_csv('smallset.csv', dtype={"value1": int, "value2": int})
        my_tuple = (df['value1'][0], df['value2'][0])
        Calculator.add_number(my_tuple)
        print(Calculator.get_last_result_value())
