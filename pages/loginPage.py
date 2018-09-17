from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base import Base


class LoginPage(Base):

    username_field = (By.ID, 'login-form-username')
    password_field = (By.ID, 'login-form-password')
    create_button = (By.ID, "create_link")
    login_button = (By.ID, "login-form-submit")
    error_message = (By.CSS_SELECTOR, "div[class='aui-message error']")

    def login(self, username, password):
        self.wait_for_visible(self.username_field).send_keys(username)
        self.wait_for_visible(self.password_field).send_keys(password)
        self.click_when_clickable(self.login_button)
        try:
            self.wait_for_visible(self.create_button)
            return True
        except TimeoutException:
            return False


