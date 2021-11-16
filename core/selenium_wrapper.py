import os
from selenium import webdriver


class SeleniumWrapper(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Singleton Pattern"""
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self, url):
        driver = webdriver.Chrome(os.path.dirname(__file__) + '/chromedriver')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        return driver
