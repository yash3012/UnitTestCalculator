"""This is the addition calculation that inherits val A & B from the calculation class"""
from calc.calculations.calculation import Calculation

# This is how you extend the Addition class with the Calculation

class Addition(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def get_result(self):
        """get result method"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
