from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import *
from selenium.webdriver.support import expected_conditions as EC
from helpers import Helpers


class LoginPage(Base):
    driver = super().driver

    username = (By.ID, 'login-form-username')
    password = (By.ID, 'login-form-password')
    create_button = (By.ID, "create_link")
    login_button = (By.ID, "login-form-submit")

    def login(self, username, password):
        self.waitForVisible.send_keys(username)
        self.waitForVisible.  send_keys(password)
        self.login_button.click()
        return self.create_button
