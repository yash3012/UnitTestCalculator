"""Calculation history Class"""
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
