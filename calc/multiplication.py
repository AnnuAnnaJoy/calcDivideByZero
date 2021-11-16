"""This is our addition class"""
from calc.calculation import Calculation


class Multiplication(Calculation):
    """Multiplication class"""

    def get_result(self):
        """multiplication """
        return self.val_a * self.val_b
