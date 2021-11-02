"""Testing the Calculator"""
from calc_main import Calculator


def test_calculator_result():
    """checking if the result for calculator is 0"""
    calc = Calculator()
    assert calc.result == 0


def test_calculator_add():
    """Check the add method of the calculator"""
    calc = Calculator()
    calc.add(1)
    assert calc.get_result() == 1


def test_calculator_get_result():
    """Check the get result method of calculator"""
    calc = Calculator()
    assert calc.get_result() == 0


def test_calculator_subtract():
    """Check the subtract method of calculator"""
    # Arrange
    calc = Calculator()
    # Act
    calc.subtract(1)
    # Assert
    assert calc.get_result() == -1


def test_calculator_multiply():
    """Test the multiply method now"""
    # Arrange
    calc = Calculator()
    # Act
    result = calc.multiply(1, 2)
    # Assert
    assert result == 2


def test_calculator_divide():
    """Test the division method"""
    # Arrange
    calc = Calculator()
    # Act
    result = calc.divide(2, 1)
    # Assert
    assert result == 2
