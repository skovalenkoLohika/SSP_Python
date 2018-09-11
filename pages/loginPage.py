from driver import Driver


class LoginPage(Driver):

    driver = super().driver

    username = driver.find_element_by_id('login-form-username')
    password = driver.find_element_by_id('login-form-password')
    create_button = driver.find_element_by_id("create_link")
    login_button = driver.find_element_by_id("login-form-submit")

    def test_login(self, username, password):
        self.driver.get("http://jira.hillel.it:8080/login.jsp")
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
        return self.create_button
