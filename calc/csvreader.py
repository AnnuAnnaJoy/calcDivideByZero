import pandas as pd
import os
from calc.calculator import Calculator


class CsvManager:
    if os.listdir(os.getcwd()):
        df = pd.read_csv('smallset.csv', dtype={"value1": int, "value2": int})
        for i in range(0, 10, 1):
            my_tuple = (df['value1'][i], df['value2'][i])
            Calculator.add_number(my_tuple)
            print(Calculator.get_last_result_value())
