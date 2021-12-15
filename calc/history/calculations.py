"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
import os
import pandas as pd
import csv
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
        """get the last calculation object from the history"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_object():
        """ get the last calculation obj from the history"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation()
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        """ get the first calculation from the history"""
        return Calculations.history[0]
    @staticmethod
    def get_calculation(number):
        """ get a specific calculation from history"""
        return Calculations.history[number]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        Calculations.write_to_csv(calculation);
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True
    @staticmethod
    def add_division_calculation(values):
        """Add a division object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True

    @staticmethod
    def write_to_csv(calc):
        """Add a division object to history using factory method create"""
        isfilecalculationHistoryExist = os.path.exists('calculation_history.csv')
        with open('calculation_history.csv', mode='a') as csv_file:
            collumnsNames = ['id', 'op','v0', 'v1','res']
            writer = csv.DictWriter(csv_file, fieldnames=collumnsNames,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if not isfilecalculationHistoryExist:
                writer.writeheader();
            writer.writerow({'id': Calculations.get_new_id_calc(),   'op':calc.operation, 'v0':calc.values[0],'v1': calc.values[1],'res':calc.get_result()})
        return True

    @staticmethod
    def get_calculation_history():
        isfilecalculationHistoryExist = os.path.exists('calculation_history.csv')
        if not isfilecalculationHistoryExist:
            return None
        dg = pd.read_csv('calculation_history.csv')
        return dg.iterrows()

    @staticmethod
    def get_new_id_calc():
        isfilecalculationHistoryExist = os.path.exists('calculation_history.csv')
        if not isfilecalculationHistoryExist:
            return 1
        dg = pd.read_csv('calculation_history.csv')
        id = len(dg.index)
        return id+1;
