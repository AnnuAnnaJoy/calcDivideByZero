"""Addition class"""
from calc.calculation.calculation import Calculation


class Addition(Calculation):

    def get_result(self):
        """ addition """
        return self.value_a + self.value_b
