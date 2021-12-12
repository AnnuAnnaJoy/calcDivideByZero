"""Division class"""
import logging
from calc.calculation.calculation import Calculation


class Division(Calculation):
    """Division class"""

    def get_result(self):
        """division """
        quotient = 0
        for index, value in enumerate(self.values):
            if index == 0:
                quotient = value
            else:
                try:
                    quotient /= value
                except ZeroDivisionError as err:
                    logging.error(
                        "Exception occurred %s %s / %s", err, self.values[0], self.values[1],
                        exc_info=True)
        return quotient
