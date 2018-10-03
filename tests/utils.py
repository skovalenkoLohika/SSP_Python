from tests.driver import DriverSetup
from pages.loginPage import LoginPage
from tests.variables import *


class Utils (DriverSetup):

    def login_to_jira(self):
        self.driver = self.driver_setup(self)
        login = LoginPage(self.driver)
        login.login(USER_NAME, PASSWORD)
