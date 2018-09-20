from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_visible_elements(self, locator):
        return self.wait.until(EC.visibility_of_any_elements_located(locator))

    def click_when_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_for_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_alert(self):
        self.wait.until(EC.alert_is_present())



