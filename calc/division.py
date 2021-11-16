"""This is our addition class"""
from calc.calculation import Calculation


class Division(Calculation):
    """Division class"""

    def get_result(self):
        """division """
        try:
            return self.value_a / self.value_b
        except ZeroDivisionError as err:
            raise ZeroDivisionError("The divisor must not be zero") from err
