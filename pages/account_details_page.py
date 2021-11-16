from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AccountDetailsPage:

    FIRST_NAME_LOC = "//input[@id='given_name']"
    LAST_NAME_LOC = "//input[@id='family_name']"
    SAVE_CHANGES_BTN_LOC = "//section[contains(@class, 'contact card')]//button"

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.FIRST_NAME_LOC)))

    def get_first_name(self):
        return self.driver.find_element_by_xpath(self.FIRST_NAME_LOC).get_attribute("value")

    def set_first_name(self, new_name):
        el = self.driver.find_element_by_xpath(self.FIRST_NAME_LOC)
        el.clear()
        el.send_keys(new_name)

    def get_last_name(self):
        return self.driver.find_element_by_xpath(self.LAST_NAME_LOC).get_attribute("value")

    def set_last_name(self, new_last_name):
        el = self.driver.find_element_by_xpath(self.LAST_NAME_LOC)
        el.clear()
        el.send_keys(new_last_name)

    def save_changes(self):
        self.driver.find_element_by_xpath(self.SAVE_CHANGES_BTN_LOC).click()


