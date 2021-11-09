"""division class"""

from calc.calculations.calculation import Calculation

# This is how you extend the division class with the Calculation

class Division(Calculation):
    """div calculation obj"""
    def get_result(self):
        """method to get division results"""
        result = 1.0
        for value in self.values:
            result = result / value
        return result
