"""This is a multiplication class """
from calc.calculation import Calculation

# This is how you extend the Addition class with the Calculation

class Multiplication(Calculation):
    """class docstring"""
    def get_result(self):
        """method"""
        return self.value_a * self.value_b
