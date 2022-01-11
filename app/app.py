"""A simple flask web app"""
from flask import Flask, request
from flask import render_template
from calc.calculator import Calculator
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/")
def index():
    """index  Route Response"""
    #return IndexController.get()
    return render_template('index.html')


@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        # get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        # make the tuple
        my_tuple = (value1, value2)
        # this will call the correct operation
        getattr(Calculator, operation)(my_tuple)
        result = str(Calculator.get_last_result_value())
        return render_template(
            'result.html', value1=value1, value2=value2, operation=operation, result=result)
        # Displays the form because if it isn't a post it is a get request

    return render_template('basicform.html')


@app.route("/bad/<value1>/<value2>")
def bad_calc(value1, value2):
    """bad calc Route Response"""
    result = value1 + value2
    response = "The result of the calculation is: " + result + '<a href="/"> back</a>'
    return response


@app.route("/good/<float:value1>/<float:value2>")
def good_calc(value1, value2):
    """good calc Route Response"""
    my_tuple = (value1, value2)
    Calculator.add_number(my_tuple)
    response = "The result of the calculation is: " \
               + str(Calculator.get_last_result_value()) + '<a href="/"> back</a>'
    return response

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()