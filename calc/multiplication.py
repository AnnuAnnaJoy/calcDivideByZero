"""This is our addition class"""
from calc.calculation import Calculation


class Multiplication(Calculation):

    def get_result(self):
        """multiplication """
        return self.a * self.b
