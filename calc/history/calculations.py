"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division

class Calculations:
    """Calculation history Class"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """ clear the history list"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """ get the length of history list"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """ get the last calculation from the history"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_object():
        """ get the last calculation obj from the history"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_result_value():
        """ get the result of last calculation from history"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        """ get the first calculation from the history"""
        return Calculations.history[0]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        """ Perform addition and add the obj to history using factory method"""
        Calculations.add_calculation(Addition.create(values))
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        """ get a specific calculation from history"""
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation(values):
        """ get a specific calculation from history"""
        Calculations.add_calculation(Multiplication.create(values))
        return True
    @staticmethod
    def add_division_calculation(values):
        """ get a specific calculation from history"""
        Calculations.add_calculation(Division.create(values))
        return True
