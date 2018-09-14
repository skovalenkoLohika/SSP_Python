from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver: WebDriver):
        self.driver  = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_when_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()


