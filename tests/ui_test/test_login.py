import pytest
from pages.loginPage import LoginPage
from variables import *


@pytest.mark.usefixtures("driver_setup")
class TestLogin:

    @pytest.mark.parametrize("username, password", [
        (PASSWORD, WRONG_USER),
        (WRONG_PASSWORD, PASSWORD),
    ])
    @pytest.mark.xfail(strict=True)
    def test_login(self, username, password):
        login = LoginPage(self.driver)
        login.login(username, password)

    def test_login(self):
        login = LoginPage(self.driver)
        login.login(USER_NAME, PASSWORD)
