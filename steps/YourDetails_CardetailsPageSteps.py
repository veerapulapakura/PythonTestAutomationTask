from typing import TextIO
import re
from behave import *
from selenium import webdriver

@when('The user read the data from the car input file')
def ReadingFile(context):
    with open('/Users/veerapulapakura/AutomationProjects/PythonWebTask_CarValuation/resources/car_inputV4.txt','r') as f:
        data = f.read()
        pattern = r'\b[A-Z]{2}\d{2}\s[A-Z]{3}\b|\b[A-Z]{1,3}\s\d{1,4}\b'
        car_numbers = re.findall(pattern, data)
        print("UK Car Numbers Found:", car_numbers)
        print(data)
        f.seek(0)
        f.write("Data added")

        #f.close()



@then('The user should be able to verify data with car output file')
def WritingData(context):
    print("Veera Pulapakura")






