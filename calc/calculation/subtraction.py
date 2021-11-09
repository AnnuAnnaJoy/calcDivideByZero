"""Subtraction class"""
from calc.calculation.calculation import Calculation


class Subtraction(Calculation):

    def get_result(self):
        """ subtraction """
        return self.value_a - self.value_b
