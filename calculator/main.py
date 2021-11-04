""" This is the calculator program"""


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        return value_b + value_a

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        return value_a - value_b

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        return value_a * value_b

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide two numbers and store the result"""
        try:
            return value_a / value_b
        except ZeroDivisionError as err:
            raise ZeroDivisionError("The divisor must not be zero") from err
