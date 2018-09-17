import pytest


from pages.loginPage import LoginPage
from variables import *


@pytest.mark.usefixtures("driver_setup")
class TestLogin:

    @pytest.mark.parametrize("username, password, expected_result", [
        (WRONG_USER, PASSWORD, False),
        (USER_NAME, WRONG_PASSWORD, False),
        (USER_NAME, PASSWORD, True)])
    def test_login(self, username, password, expected_result):
        login = LoginPage(self.driver)
        result = login.login(username, password)
        assert (result == expected_result)

