"""This main.py file tests if the calculator can do calculations properly"""
import time
import pandas as pd
from pathlib import Path
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


add= pd.read_csv("tests/test_data/addition.csv")[:30]
sub= pd.read_csv("tests/test_data/subtraction.csv")[:30]
mul= pd.read_csv("tests/test_data/multiplication.csv")[:30]
div= pd.read_csv("tests/test_data/division.csv")[:30]

try:
    result_directory = Path("log_files/")
    result_directory.mkdir(parents = True, exist_ok = True)

    result_output_directory = Path("after_test/")
    result_output_directory.mkdir(parents = True, exist_ok = True)

except:
    print("Directories Already Present")
name_of_files= ["addition.csv", "subtraction.csv", "multiplication.csv", "division.csv"]
files_for_calc= [add, sub, mul, div]
operations=[Addition, Subtraction, Multiplication, Division]
for i in range(len(name_of_files)):
    name = name_of_files[i]
    print(name + " Process Running")
    t = time.time()
    #print(t)
    file_for_log = open("log_files/Log.txt", "a", encoding="utf-8")  # pylint: disable= consider-using-with
    file_for_log.write("\nUNIX_time_stamp " + str(t) + "\t File_name: " + name + "\n")
    file_for_log.write("Record_No" + "\t" + "Value_1" + "\t" + "Value_2" + "\t"
                       + "Operation" + "\t" + "Result" + "\n")
    if i == 3:
        file_for_exceptions = open("log_files/EXC_Log.txt", "a", encoding="utf-8")  # pylint: disable= consider-using-with
        file_for_exceptions.write("\nUNIX_time_stamp " + str(t) + "\t File_name: " + name + "\n")
        file_for_exceptions.write("Record_No" + "\t" + "Value_1" + "\t" + "Value_2"
                                  + "\t" + "Operation" + "\t" + "Result" + "\n")

    for j in range(len(files_for_calc[i])):

        nums= (files_for_calc[i]['value_1'][j], files_for_calc[i]['value_2'][j])

        if i == 3:

            try:
                division = Division(nums)
                result = division.get_result()
                file_for_log.write(str(j) + "\t" + str(nums[0]) + "\t" + str(nums[1])
                                   + "\t" + (name_of_files[i][:-4]) + "\t" + str(result) + "\n")
                files_for_calc[i].to_csv("after_test/" + name_of_files[i])

            except ZeroDivisionError:
                file_for_exceptions.write(str(j) + "\t" + str(nums[0]) + "\t" + str(nums[1])
                                          + "\t" + (name_of_files[i][:-4]) + "\t" + "ZeroDivisionError" + "\n")
            continue

        calculations = operations[i](nums)
        results= calculations.get_result()

        file_for_log.write(str(j) + "\t" + str(nums[0]) + "\t" + str(nums[1])
                           + "\t" + (name_of_files[i][:-4]) + "\t" + str(results) + "\n")
    files_for_calc[i].to_csv("after_test/" + name_of_files[i])
file_for_log.close()
