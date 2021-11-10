"""Division class"""
from calc.calculation.calculation import Calculation


class Division(Calculation):

    def get_result(self):
        """division """
        quotient = 1
        try:
            for value in self.values:
                quotient /= value
            return quotient
        except ZeroDivisionError as err:
            raise ZeroDivisionError("The divisor must not be zero") from err
