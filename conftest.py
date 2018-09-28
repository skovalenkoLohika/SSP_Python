import pytest
from selenium.webdriver.remote.webdriver import WebDriver
import allure


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    driver: WebDriver = item.instance.driver
    if rep.when in 'call':
        allure.attach(driver.get_screenshot_as_png(),
                      name=item._pyfuncitem.name,
                      attachment_type=allure.attachment_type.PNG)
