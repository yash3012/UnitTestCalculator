"""This is our calculation base class / Abstract Class"""
class Calculation: # pylint: disable=too-few-public-methods
    """class docstring"""

    #contstructor and it is the first function called when an object of the class is instantiated

    def __init__(self, value_a, value_b):
        """method"""
        #self references the instantiated object of the class
        self.value_a = value_a
        self.value_b = value_b


    @classmethod
    def create(cls, value_a, value_b):
        """docstring"""
        return cls(value_a,value_b)
