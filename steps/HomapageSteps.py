from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when('The user is on the home page of webuyanycar')
def Homepage(context):
    try:
        context.driver = webdriver.Chrome()
        context.driver.get("https://www.webuyanycar.com/")
        context.driver.maximize_window()
        context.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        context.driver.find_element(By.ID, "vehicleReg").send_keys(context.car_numbers_extracted[0])
        context.driver.find_element(By.ID, "Mileage").send_keys("50000")
        context.driver.find_element(By.ID, "btn-go").click()
        context.driver.find_element(By.ID, "EmailAddress").send_keys("veera.ratna@gmail.com")
        context.driver.implicitly_wait(10)
        context.driver.quit()
    finally:
        print("An exception occurred")
















