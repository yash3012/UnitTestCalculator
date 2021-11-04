"""This is a test class"""
import pytest

from calculator.calculator import Calculator

@pytest.fixture
def clear_history():
    """method for clearing history"""
    Calculator.clear_history()


def test_calculator_add():
    """test the addition function"""
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6


def test_clear_history():
    """clear"""
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    Calculator.clear_history()
    assert Calculator.history == []


def test_count_history():
    """clear"""
    assert Calculator.history_count() == 0
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.history_count() == 2


def test_get_last_calculation_result():
    """clear"""
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.get_last_calculation_result() == 5


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_numbers(2, 1) == 1


def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 2) == 2


def test_calculator_divide():
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(2, 1) == 2


def test_get_first_calculation():
    """testing to see the first calculation in history"""
    assert Calculator.get_first_calculation() == Calculator.history[0]


def test_get_last_calculation_object():
    """testing to verify the last calculation in the history"""
    assert Calculator.get_last_calculation() == Calculator.history[Calculator.history_count() - 1]


def add_calculation_to_history():
    """testing to see if calculations are added to history before & after calculation"""
    previous_length = len(Calculator.history)
    Calculator.add_numbers(1, 2)
    assert len(Calculator.history) == previous_length + 1


def get_first_calculation():
    """test to get the first calculation"""
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    calculation = Calculator.history[0]
    assert calculation.get_result == 3


def get_last_calculation():
    """test to get the last calculation"""
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    calculation = Calculator.history[Calculator.history_count() - 1]
    assert calculation.get_result == 6
