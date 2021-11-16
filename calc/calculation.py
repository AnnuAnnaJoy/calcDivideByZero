"""This is our base class"""


class Calculation:
    """Calculation class"""
    result = 0

    def __init__(self, val_a, val_b):
        self.val_a = val_a
        self.val_b = val_b

    @classmethod
    def create(cls, val_a, val_b):
        """Using class method to create objects of all individual operations"""
        return cls(val_a, val_b)

    @property
    def value_a(self):
        """Getter For Value A"""
        return self.val_a

    @property
    def value_b(self):
        """Getter For Value B"""
        return self.val_b
