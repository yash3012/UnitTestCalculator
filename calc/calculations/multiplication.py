"""This is a multiplication class """
from calc.calculations.calculation import Calculation

# This is how you extend the Addition class with the Calculation

class Multiplication(Calculation):
    """class docstring"""
    def get_result(self):
        """method"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
