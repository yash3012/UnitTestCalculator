"""Calculation Class"""
class Calculation:
    """ calculation abstract base class"""
    # pylint: disable=too-few-public-methods
    def __init__(self,values: tuple):
        """Constructor method"""
        # print instance of this class
        self.values = Calculation.convert_args_to_tuple_float(values)
        self.operation = type(self).__name__

    @classmethod
    def create(cls, values: tuple):
        """Factory method"""
        return cls(values)

    @staticmethod
    def convert_args_to_tuple_float(values):
        """ Standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
