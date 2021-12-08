import pandas as pd
import os
from calc.calculator import Calculator


class CsvManager:
    @staticmethod
    def csv_process(operators):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "inputFile")
        file_loc = os.path.join(file_path, "smallset.csv")
        if os.listdir(file_path):
            # print(os.listdir(file_path))
            df = pd.read_csv(file_loc, dtype={"sno": int, "value1": int, "value2": int})
            df.set_index('sno', inplace=True)
            my_tuple = ()
            if operators is None:
                operators = '1'
            storedict = [0] * (len(df) + 1)
            for i in range(len(df) + 1):
                try:
                    my_tuple = (df['value1'][i], df['value2'][i])
                except KeyError as err:
                    print(err)
                if operators == '1':
                    Calculator.add_number(my_tuple)
                elif operators == '2':
                    Calculator.subtract_number(my_tuple)
                elif operators == '3':
                    Calculator.multiply_numbers(my_tuple)
                else:
                    Calculator.divide_numbers(my_tuple)
                res = Calculator.get_last_result_value()
                storedict[i] = res

            df1 = pd.DataFrame(df[['value1', 'value2']])
            df2 = pd.DataFrame(storedict, columns=['result'])
            df3 = pd.concat([df1, df2], axis=1)
            # print(df3[1:len(df)+1])
            df3[1:len(df) + 1].to_csv('calc/utils/resultFile/results.csv', index_label='sno')
