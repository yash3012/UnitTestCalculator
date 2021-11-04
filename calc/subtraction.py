"""This is a subtraction class"""
from calc.calculation import Calculation

# This is how you extend the subtraction class with the Calculation

class Subtraction(Calculation):
    """class docstring"""
    def get_result(self):
        """method"""
        return self.value_a - self.value_b
