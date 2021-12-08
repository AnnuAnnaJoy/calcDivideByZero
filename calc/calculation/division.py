"""Division class"""
from calc.calculation.calculation import Calculation


class Division(Calculation):
    """Division class"""

    def get_result(self):
        """division """
        quotient = 0
        try:
            for index, value in enumerate(self.values):
                if index == 0:
                    quotient = value
                else:
                    quotient /= value
            return quotient
        except ZeroDivisionError as err:
            raise err
