"""Testing Multiplication Method"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing if the calculator has a static method for multiplication"""
    #Arrange
    my_nums = (2.0,3.0)

    #Act
    multiplication = Multiplication(my_nums)

    #Assert
    assert multiplication.get_result() == 6.0
