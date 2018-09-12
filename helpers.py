from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import Driver


class Helpers(Driver):
    driverPath = "WebDrivers/chromedriver_win.exe"
    driver = WebDriver
    wait = WebDriverWait(driver, 10)

    def waitForVisible(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))

    def clickWhenClicable(self, element):
        self.wait.until(EC.element_to_be_clickable(element)).click()
