import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class Driver:

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")

    if os.name == 'nt':
        driverPath = "WebDrivers/chromedriver_win.exe"
    else:
        driverPath = "WebDrivers/chromedriver_linux"

    try:
        driver = webdriver.Chrome(executable_path=driverPath, chrome_options=options)
    except WebDriverException:
        print("failed to start driver at " + driverPath)

