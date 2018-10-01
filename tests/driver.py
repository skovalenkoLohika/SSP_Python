import os
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverSetup:
    driver = None

    def driver_setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument("start-maximized")
        try:
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
            self.driver.get("http://jira.hillel.it:8080/login.jsp")
        except WebDriverException:
            print("failed to start driver")
        return self.driver
