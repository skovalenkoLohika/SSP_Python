import os
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def driver_setup(request):
    driver = None
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument("start-maximized")
    if os.name == "nt":
        driver_path = "../../WebDrivers/chromedriver_win.exe"
    else:
        driver_path = "WebDrivers/chromedriver_linux"
    try:
        driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
        driver.get("http://jira.hillel.it:8080/login.jsp")
    except WebDriverException:
        print("failed to start driver at " + driver_path)
    request.cls.driver = driver

    yield driver
    driver.close()

