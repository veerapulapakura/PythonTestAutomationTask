from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class PageFactory:
    pass


class HopePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        PageFactory.init_elements(driver, self)  # Initialize elements using Page Factory

    # Define locators using FindsBy annotations
    #username_field = FindsBy(by=By.ID, value="username")
    #password_field = FindsBy(by=By.ID, value="password")
    #login_button = FindsBy(by=By.XPATH, value="//button[text()='Login']")
