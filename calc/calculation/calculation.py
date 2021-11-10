"""This is our base class"""


class Calculation:
    result = 0

    """ Constructor"""

    def _init_(self, values: tuple):
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    """ Add method"""

    @classmethod
    def create(cls, values: tuple):
        """Using class method to create objects of all individual operations"""
        return cls(values)

    @staticmethod
    def convert_args_to_tuple_of_float(values):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
