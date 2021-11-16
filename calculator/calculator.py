""" This is the calculator program"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division
from history.historycalc import History


class Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        # create an addition object using the factory we created on the calculation class
        addition = Addition.create(value_a, value_b)
        History.add_calculation_to_history(addition)
        return History.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        History.add_calculation_to_history(subtraction)
        return History.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        multiplication = Multiplication.create(value_a, value_b)
        History.add_calculation_to_history(multiplication)
        return History.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide two numbers and store the result"""
        division = Division.create(value_a, value_b)
        History.add_calculation_to_history(division)
        return History.get_result_of_last_calculation_added_to_history()
