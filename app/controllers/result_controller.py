from app.controllers.controller import ControllerBase
from flask import render_template

from calc.calculator import Calculator
from calc.utils.csvmanager import CsvManager


class ResultController(ControllerBase):
    @staticmethod
    def get():
        df = CsvManager.read_resultcsv()
        results = []
        for _, row in df.iterrows():
            function_handler = getattr(Calculator, row.operation)

            try:
                function_handler((row.value1, row.value2))
                result = str(Calculator.get_last_result_value())
            except ZeroDivisionError:
                result = 'ZeroDivisionError'
            resulttup = (str(row.value1), str(row.value2), str(row.operation), result)
            results.append(resulttup)
        return render_template('result.html', results=results)
