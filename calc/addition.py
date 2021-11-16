"""This is our addition class"""
from calc.calculation import Calculation


class Addition(Calculation):
    """addition"""
    def get_result(self):
        """ addition """
        return self.value_a + self.value_b
