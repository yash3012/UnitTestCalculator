""" This is the file for performing operation"""
class Calculator:
    """ This is the Calculator class"""

    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result


    def add(self, val_a):
        """ adds number to result"""
        self.result = self.result + val_a
        return self.result


    def subtract(self, val_a):
        """ subtract number from result"""
        self.result = self.result - val_a
        return self.result


    def multiply(self, val_a, val_b):
        """ multiply two numbers and store the result"""
        self.result = val_a * val_b
        return self.result

    def divide(self, val_a, val_b):
        """divide the two numbers and store the result"""
        self.result = val_a / val_b
        return self.result
