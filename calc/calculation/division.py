"""Division class"""
import os
import logging
from calc.calculation.calculation import Calculation
from calc.utils.csvmanager import CsvManager

logging.basicConfig(
    filename='result_logs/app.log', filemode='w', level=logging.NOTSET,
    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


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
                        "Exception occurred in file %s during operation %s %s / %s",
                        os.listdir(CsvManager.path_file()), err, self.values[0],
                        self.values[1], exc_info=True)
                    quotient = 'ZeroDivisionError'
        return quotient
