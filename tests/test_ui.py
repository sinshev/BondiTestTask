import pytest

from core.selenium_wrapper import SeleniumWrapper
from core import config
from pages.login_page import LoginPage
from pages.account_details_page import AccountDetailsPage
from core.utils import get_random_name


class TestSystem76:

    HOST_URL = "https://system76.com"
    ACCOUNT_DETAILS_URL = HOST_URL + "/my-account/edit"
    LOGIN_URL = "https://account.system76.com/login"

    def setup_class(self):
        selenium_driver = SeleniumWrapper()
        self.driver = selenium_driver.connect(self.LOGIN_URL)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture
    def login(self):
        login_page = LoginPage(self.driver)
        login_page.login(config.EMAIL, config.PASSWORD)

    def test_smoke(self, login):
        self.driver.get(self.ACCOUNT_DETAILS_URL)
        account_details_page = AccountDetailsPage(self.driver)
        old_name = account_details_page.get_first_name()
        old_last_name = account_details_page.get_last_name()

        new_name = get_random_name()
        new_last_name = get_random_name()

        account_details_page.set_first_name(new_name)
        account_details_page.set_last_name(new_last_name)
        account_details_page.save_changes()

        # navigate away and back to the page
        self.driver.get(self.HOST_URL)
        self.driver.get(self.ACCOUNT_DETAILS_URL)

        current_name = account_details_page.get_first_name()
        current_last_name = account_details_page.get_last_name()

        assert current_name != old_name
        assert current_name == new_name

        assert current_last_name != old_last_name
        assert current_last_name == new_last_name
