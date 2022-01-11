"""Subtraction class"""
from calc.calculation.calculation import Calculation


class Subtraction(Calculation):
    """Subtraction class"""

    def get_result(self):
        """ subtraction """
        total_diff = 0
        for index, value in enumerate(self.values):
            if index == 0:
                total_diff = value
            else:
                total_diff -= value
        return total_diff
