import pytest
from pages.loginPage import LoginPage
from variables import *


@pytest.mark.usefixtures("driver_setup")
class TestLogin:

    @pytest.mark.parametrize("username, password", [
        (PASSWORD, WRONG_USER),
        (WRONG_PASSWORD, PASSWORD),
        (USER_NAME, PASSWORD)
    ])
    def test_login(self, username, password):
        login = LoginPage(self.driver)
        create_button = login.login(username, password)
        assert create_button is not None

