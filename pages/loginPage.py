from selenium import webdriver
from driver import Driver

driver = webdriver.Chrome()


class LoginPage(Driver):

    username = driver.find_element_by_id('login-form-username')
    password = driver.find_element_by_id('login-form-password')
    create_button = driver.find_element_by_id("create_link")
    login_button = driver.find_element_by_id("login-form-submit")

    def login(self, username, password):
        driver.get("http://jira.hillel.it:8080/login.jsp")
        self.username.send_keys(username)
        self.password.send_keys(password)

        return self.create_button

