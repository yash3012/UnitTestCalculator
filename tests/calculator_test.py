"""This is a test class"""

from calculator.calculator import Calculator


def test_calculator_add():
    """test the addition function"""
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6


def test_get_history():
    """test the history of calculation"""
    assert Calculator.clear_history()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    assert Calculator.get_history()


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
    assert Calculator.add_numbers(3, 3) == 6
    assert Calculator.get_last_calculation_result() == 6


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_numbers(2, 1) == 1
    assert Calculator.subtract_numbers(2, 2) == 0
    assert Calculator.subtract_numbers(5, 1) == 4


def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 2) == 2


def test_calculator_divide():
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(2, 1) == 2
    assert Calculator.divide_numbers(2, 2) == 1


def test_get_first_calculation():
    """testing to see if the first calculation in history is being stored"""
    Calculator.clear_history()
    Calculator.add_numbers(1, 1)
    Calculator.add_numbers(1, 2)
    assert Calculator.get_first_calculation() == Calculator.history[0]


def test_get_last_calculation_object():
    """testing to verify the last calculation in the history"""
    Calculator.clear_history()
    Calculator.add_numbers(5, 5)
    Calculator.add_numbers(6, 3)
    last_indx = Calculator.history_count() - 1
    assert Calculator.get_last_calculation_object() == Calculator.history[last_indx]


def test_add_calculation_to_history():
    """testing to see if calculations are added to history before & after calculation"""
    Calculator.clear_history()
    previous_length = len(Calculator.history)
    Calculator.add_numbers(1, 2)
    assert len(Calculator.history) == previous_length + 1


def test_get_last_calculation():
    """test to get the last calculation"""
    Calculator.clear_history()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    assert Calculator.get_last_calculation() == Calculator.history[-1]
