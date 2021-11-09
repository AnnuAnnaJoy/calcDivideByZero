"""This is our base class"""


class Calculation:
    result = 0

    """ Constructor"""

    def _init_(self, a, b):
        self.a = a
        self.b = b

    """ Add method"""

    @classmethod
    def create(cls, a, b):
        """Using class method to create objects of all individual operations"""
        return cls(a, b)

    @property
    def value_a(self):
        """Getter For Value A"""
        return self.a

    @property
    def value_b(self):
        """Getter For Value B"""
        return self.b
