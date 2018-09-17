from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_when_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_for_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))


