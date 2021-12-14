"""CSV calc"""
import pandas as pd
from calc.calculator import Calculator


class CsvCalc:
    """ CSV calculation process"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def csvprocess(dataf, operators):
        """process"""
        my_tuple = ()
        storedict = [0] * (len(dataf) + 1)
        for i in range(len(dataf) + 1):
            try:
                my_tuple = (dataf['value1'][i], dataf['value2'][i])
            except KeyError as err:
                print(err)
            if operators == 1:
                Calculator.addition(my_tuple)
            elif operators == 2:
                Calculator.subtraction(my_tuple)
            elif operators == 3:
                Calculator.multiplication(my_tuple)
            else:
                Calculator.division(my_tuple)
            res = Calculator.get_last_result_value()
            storedict[i] = res

        df1 = pd.DataFrame(dataf[['value1', 'value2']])
        df2 = pd.DataFrame(storedict, columns=['result'])
        df3 = pd.concat([df1, df2], axis=1)
        return df3
