"""This is a subtraction class"""
from calc.calculations.calculation import Calculation

# This is how you extend the subtraction class with the Calculation

class Subtraction(Calculation):
    """class docstring"""
    def get_result(self):
        """method to get subtraction result"""
        diff_of_values = 0.0
        for value in self.values:
            diff_of_values = diff_of_values - value
        return diff_of_values
