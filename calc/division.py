"""division class"""

from calc.calculation import Calculation

# This is how you extend the division class with the Calculation

class Division(Calculation):
    """class docstring"""
    def get_result(self):
        """method"""
        return self.value_a / self.value_b
