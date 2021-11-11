"""Division class"""
from calc.calculation.calculation import Calculation


class Division(Calculation):
    """Division class"""

    def get_result(self):
        """division """
        quotient = 1
        try:
            for value in self.values:
                quotient /= value
            return quotient
        except ZeroDivisionError as err:
            raise err
