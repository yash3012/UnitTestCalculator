""" This is the file for performing operation"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class Calculator:
    """This is the Calculator class"""
    history = []


    @staticmethod
    def get_history():
        """get the history"""
        get_history = Calculator.history
        return get_history

    @staticmethod
    def get_first_calculation():
        """return the first calculation from the history list"""
        return Calculator.history[0]

    @staticmethod
    def get_last_calculation():
        """return the last calculation from the history list"""
        return Calculator.history[Calculator.history_count() - 1]

    @staticmethod
    def add_calculation_to_history(calculation):
        """method to add calculation to history"""
        Calculator.history.append(calculation)
        return True


    @staticmethod
    def get_last_calculation_result():
        """gets the result of the last/most recent calculation stored in the history"""
        result_obj = Calculator.get_last_calculation()
        return result_obj.get_result()

    @staticmethod
    def get_last_calculation_object():
        """this method return the object of the last calculation"""
        result_object = Calculator.get_last_calculation()
        return result_object

    @staticmethod
    def clear_history():
        """clears the history list of calculation"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """method to count the length of the history"""
        return len(Calculator.history)

    @staticmethod
    def add_numbers(value_a, value_b):
        """ returns the sum of two numbers"""
        addition = Addition(value_a,value_b)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ returns the difference of the two numbers"""
        subtraction = Subtraction(value_a,value_b)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ returns the product of two numbers"""
        multiplication = Multiplication(value_a,value_b)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ returns the division of two numbers"""
        division = Division(value_a,value_b)
        Calculator.history.append(division)
        return division.get_result()
