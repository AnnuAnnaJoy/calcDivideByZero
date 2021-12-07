import pandas as pd
import os
from calc.calculator import Calculator


class CsvManager:

    if os.listdir(os.getcwd()):
        # print(os.listdir(os.getcwd()))
        df = pd.read_csv('Utility/smallset.csv', dtype={"sno": int, "value1": int, "value2": int})
        df.set_index('sno', inplace=True)
        my_tuple = ()
        storeDict = [0] * (len(df)+1)
        for i in range(len(df)+1):
            try:
                my_tuple = (df['value1'][i], df['value2'][i])
            except KeyError as err:
                print(err)
            Calculator.add_number(my_tuple)
            res = Calculator.get_last_result_value()
            storeDict[i] = res

        df1 = pd.DataFrame(df[['value1', 'value2']])
        df2 = pd.DataFrame(storeDict, columns=['result'])
        df3 = pd.concat([df1, df2], axis=1)
        #print(df3[1:len(df)+1])
        df3[1:len(df)+1].to_csv('Utility/results.csv', index_label='sno')
