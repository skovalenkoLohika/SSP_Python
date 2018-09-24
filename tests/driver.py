import os
from selenium.common.exceptions import WebDriverException
from selenium import webdriver


class DriverSetup:
    driver = None

    def driver_setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument("start-maximized")
        if os.name == "nt":
            driver_path = ".\\WebDrivers\\chromedriver_win.exe"
        else:
            driver_path = "./WebDrivers/chromedriver_linux"
        try:
            self.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
            self.driver.get("http://jira.hillel.it:8080/login.jsp")
        except WebDriverException:
            print("failed to start driver at " + driver_path)
        return self.driver



