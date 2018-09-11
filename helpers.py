from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from driver import Driver


class Helpers(Driver):

    driver = super().driver

    def click_when_clicable(self, element):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(element)).click()
