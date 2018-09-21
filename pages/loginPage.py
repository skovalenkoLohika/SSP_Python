from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base import Base


class LoginPage(Base):

    _username_field = (By.ID, 'login-form-username')
    _password_field = (By.ID, 'login-form-password')
    _create_button = (By.CSS_SELECTOR, "a[id=create_link]")
    _login_button = (By.ID, "login-form-submit")
    _result = (By.CSS_SELECTOR, "div[class='aui-message error'], a[id=create_link]")

    def login(self, username, password):
        self.wait_for_visible(self._username_field).send_keys(username)
        self.wait_for_visible(self._password_field).send_keys(password)
        self.click_when_clickable(self._login_button)
        result = self.wait_for_visible(self._result)
        if result.get_attribute('class') == 'aui-message error':
            return False
        else:
            return True


