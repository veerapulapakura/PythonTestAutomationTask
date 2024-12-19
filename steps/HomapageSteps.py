from behave import *
from selenium import webdriver
#from selenium.webdriver.common.by import By


@given('The user is on the home page of webuyanycar')
def Homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.webuyanycar.com/")










