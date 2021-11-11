"""Subtraction class"""
from calc.calculation.calculation import Calculation


class Subtraction(Calculation):
    """Subtraction class"""

    def get_result(self):
        """ subtraction """
        total_diff = 2 * self.values[0]
        for value in self.values:
            total_diff -= value
        return total_diff
