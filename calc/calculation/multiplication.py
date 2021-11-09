"""Multiplication class"""
from calc.calculation.calculation import Calculation


class Multiplication(Calculation):

    def get_result(self):
        """multiplication """
        return self.a * self.b
