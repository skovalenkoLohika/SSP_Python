import pytest


from pages.loginPage import LoginPage
from variables import *


@pytest.mark.usefixtures("driver_setup")
class TestLogin:

    @pytest.mark.parametrize("username, password", [
        (WRONG_USER, PASSWORD),
        (USER_NAME, WRONG_PASSWORD)
    ])
    def test_login_failed(self, username, password):
        login = LoginPage(self.driver)
        login.login_failed(username, password)

    def test_login(self):
        login = LoginPage(self.driver)
        login.login(USER_NAME, PASSWORD)

