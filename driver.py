import os

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class Driver:

    driver = None
    driverPath = ''

    @pytest.fixture(scope="cls", autouse=True)
    def driver_setup(self, request):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        if os.name == "nt":
            self.driverPath == "WebDrivers/chromedriver_win.exe"
        else:
            self.driverPath == "WebDrivers/chromedriver_linux"

        try:
            self.driver = webdriver.Chrome(executable_path=self.driverPath, chrome_options=options)
        except WebDriverException:
            print("failed to start driver at " + self.driverPath)

        def resource_teardown():
            self.driver.quit()
        request.addfinalizer(resource_teardown)
        return self.driver
