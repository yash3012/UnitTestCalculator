"""division class"""

from calc.calculations.calculation import Calculation

# This is how you extend the division class with the Calculation

class Division(Calculation):
    """div calculation obj"""
    def get_result(self):
        """method to get division results"""
        result = self.values[0] / self.values[1]
        return result
