"""Multiplication class"""
from calc.calculation.calculation import Calculation


class Multiplication(Calculation):
    """multiplication class"""

    def get_result(self):
        """multiplication """
        total_product = 1
        for value in self.values:
            total_product *= value
        return total_product
