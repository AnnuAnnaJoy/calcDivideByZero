"""Addition class"""
from calc.calculation.calculation import Calculation


class Addition(Calculation):
    """Addition class"""

    def get_result(self):
        """ addition """
        total_sum = 0.0
        for value in self.values:
            total_sum += value
        return total_sum
