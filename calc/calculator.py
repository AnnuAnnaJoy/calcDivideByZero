""" This is the calculator program"""
from calc.historymod.history import History


class Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def addition(tuple_values: tuple):
        """ adds number to result"""
        # create an addition object using the factory we created on the calculation class
        History.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtraction(tuple_values: tuple):
        """ subtract number from result"""
        History.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiplication(tuple_values: tuple):
        """ multiply two numbers and store the result"""
        History.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def division(tuple_values: tuple):
        """ divide two numbers and store the result"""
        History.add_division_calculation(tuple_values)
        return True

    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # don't need more than one action per function
        return History.get_last_calculation_result_value()
