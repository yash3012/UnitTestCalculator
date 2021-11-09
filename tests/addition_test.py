"""Testing Addition method"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing if the calculator has a static method for addition"""
    #Arrange
    my_nums = (5.0,1.0,2.0)

    #Act
    addition = Addition(my_nums)

    #Assert
    assert addition.get_result() == 8.0
