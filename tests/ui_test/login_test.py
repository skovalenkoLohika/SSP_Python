import pytest
from pages.loginPage import *
from variables import *

login = LoginPage()
class Login:

    @pytest.mark.parametrize("username,password", [
        (USER_NAME, PASSWORD),
        (PASSWORD, WRONG_USER),
        (WRONG_PASSWORD, PASSWORD),
    ])
    def test_login(self, username, password):
        header = login.login(username, password)
        assert header is not None

