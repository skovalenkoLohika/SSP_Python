import pytest
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from tests.JsonGenerator import JsonGenerator
from tests.request_api import Api
from tests.variables import *
request_api = Api()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    driver: WebDriver = item.instance.driver
    if driver is not None:
        if rep.when in 'call' and rep.failed:
            allure.attach(driver.get_screenshot_as_png(),
                          name=item._pyfuncitem.name,
                          attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope='class')
def issues(request):
    id_issue = []
    for i in summary:
        response = request_api.create_issue(JsonGenerator.create_issue(i))
        if response.status_code == 201:
            id_issue.append(response.json().get("key"))
        else:
            print("Issue has not been created:"+response.json().text)

    def cleanup():
        if len(id_issue) > 0:
            for i in id_issue:
                request_api.delete_issue(i)
    request.addfinalizer(cleanup)
