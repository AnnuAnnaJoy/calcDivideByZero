from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for, session

from calc.utils.csvmanager import CsvManager


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        print(request.form['value1'])
        print(request.form['value2'])
        print(request.form['operation'])
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
            return render_template('calc.html', error=error)
        elif request.form['value2'] == '0' and request.form['operation'] == 'division':
            flash("Division by zero!")
            return render_template('calc.html')
        else:
            flash("Calculation Successful!")
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            input_tuple = (value1, value2, operation)
            CsvManager.writecalctocsv(input_tuple, columns=['value1', 'value2', 'operation'])
            return render_template('calc.html',  value1=value1, value2=value2,
                                   operation=operation, result=result)

    @staticmethod
    def get():
        return render_template('calc.html')
