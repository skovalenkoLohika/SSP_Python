from selenium import webdriver
from driver import Driver

driver = webdriver.Chrome()


class LoginPage(Driver):

    username = driver.find_element_by_id('login-form-username')
    password = driver.find_element_by_id('login-form-password')
    create_button = driver.find_element_by_id("create_link")

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        return self.create_button

