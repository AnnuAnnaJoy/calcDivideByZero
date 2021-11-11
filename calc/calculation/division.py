"""Division class"""
from calc.calculation.calculation import Calculation


class Division(Calculation):
    """Division class"""

    def get_result(self):
        """division """
        quotient = self.values[0] * self.values[0]
        try:
            for value in self.values:
                quotient /= value
            return quotient
        except ZeroDivisionError as err:
            raise err
