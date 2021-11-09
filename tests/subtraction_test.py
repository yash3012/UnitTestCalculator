"""Testing Subtraction Method"""
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing if the calculator has a static method for subtraction"""
    #Arrange
    my_nums = (4.0, 2.0)

    #Act
    subtraction = Subtraction(my_nums)

    #Assert
    assert subtraction.get_result() == -6
