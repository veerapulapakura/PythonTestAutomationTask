from typing import TextIO
import re
from behave import *
from selenium import webdriver

@when('The user read the data from the car input file')
def ReadingFile(context):
    with open('/Users/veerapulapakura/AutomationProjects/PythonWebTask_CarValuation/resources/car_inputV4.txt','r') as f:
        data = f.read()
        pattern_carnumbers = r'\b[A-Z]{2}\d{2}\s[A-Z]{3}\b|\b[A-Z]{1,3}\s\d{1,4}\b|[A-Z]{2}\d{2}[A-Z]{3}\b'
        context.car_numbers_extracted = re.findall(pattern_carnumbers, data)
        print("UK Car Numbers found in the file is :", context.car_numbers_extracted)
        f.write("Data extracted from the file")


@then('The user should be able to verify data with car output file')
def WritingData(context):
    print("Printing ...")
    print(context.car_numbers_extracted)






