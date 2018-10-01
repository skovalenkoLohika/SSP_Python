import pytest
import allure
from tests.variables import *
from tests.request_api import Api
from pages.issuePage import IssuePage
from pages.loginPage import LoginPage
from tests.driver import DriverSetup
from tests.JsonGenerator import JsonGenerator
request = Api()


@allure.story("Issue Tests")
@pytest.mark.ua
class TestIssues(DriverSetup):

    id_issue = []
    summary = ['Serg_Summary1', 'Serg_Summary2', 'Serg_Summary3']

    def setup_class(self):
        self.driver = self.driver_setup(self)
        login = LoginPage(self.driver)
        login.login(USER_NAME, PASSWORD)
        for i in self.summary:
            response = request.create_issue(JsonGenerator.create_issue(i))
            if response.status_code == 201:
                self.id_issue.append(response.json().get("key"))


   # with missing required fields## with parameter text length longer than supported
    @allure.step
    @allure.title("Create Issue")
    @pytest.mark.parametrize("summary, expected_message", [
        ('', "You must specify a summary of the issue."),
        ('SergSummary'*35, "Summary must be less than 255 characters."),
        ("Serg_Summary4", "Serg_Summary4")])
    def test_create_issue(self, summary, expected_message):
        issue = IssuePage(self.driver)
        message = issue.create_issue(summary)
        print('message={}'.format(message))
        if message['data-issue-key'] is not None:
            self.id_issue.append(message['data-issue-key'])
        assert expected_message in message['text']

    @allure.step
    @allure.title("Search Issue")
    @pytest.mark.parametrize("summary, search_result", [
       ('Serg_Summary1', 1),
       ('Serg_Summary*', 4),
       ('Serg111111', 0)])
    def test_search_issue(self, summary, search_result):
        issue = IssuePage(self.driver)
        assert (issue.search_issue(summary) == search_result)

    @allure.step
    @allure.title("Update Issue")
    def test_update_issue(self, search_issue="Serg_Summary1",
                         new_summary="Serg_Summary5",
                         new_priority='High',
                         assignee="Kovalenko Sergey"):
        issue = IssuePage(self.driver)
        result = issue.update_issue(search_issue, new_summary, new_priority, assignee)
        assert new_summary in result
        assert new_priority in result
        assert assignee in result

    def teardown_class(self):
        if len(self.id_issue) > 0:
            for i in self.id_issue:
                request.delete_issue(i)
        self.driver.close()




