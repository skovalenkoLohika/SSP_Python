import pytest
import allure
from pages.loginPage import LoginPage
from tests.variables import *
from tests.driver import DriverSetup


@pytest.mark.ua
@allure.feature('Login')
class TestLogin(DriverSetup):

    def setup_class(self):
        self.driver = self.driver_setup(self)

    @allure.step
    @allure.title("Login test")
    @pytest.mark.parametrize("username, password, expected_result", [
        # (WRONG_USER, PASSWORD, False),
        (USER_NAME, WRONG_PASSWORD, False)])
        # (USER_NAME, PASSWORD, True)])
    def test_login(self, username, password, expected_result):
        login = LoginPage(self.driver)
        result = login.login(username, password)
        assert (result == expected_result)

    def teardown_class(self):
        self.driver.close()
