from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    EMAIL_LOC = "//input[@id='user_email']"
    PASSWORD_LOC = "//input[@id='user_password']"
    LOGIN_BTN_LOC = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.EMAIL_LOC)))

    def login(self, email, password):
        self.driver.find_element_by_xpath(self.EMAIL_LOC).send_keys(email)
        self.driver.find_element_by_xpath(self.PASSWORD_LOC).send_keys(password)
        self.driver.find_element_by_xpath(self.LOGIN_BTN_LOC).click()
