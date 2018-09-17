import pytest
from JsonGenerator import *
from request_api import Api
from pages.issuePage import IssuePage
request = Api()


@pytest.mark.usefixtures("driver_setup")
class TestIssues:

   # prepare issues for search
   #  @pytest.mark.parametrize("summary", [
   #      ('Serg_Summary1'),
   #      ('Serg_Summary2'),
   #      ('Serg_Summary3'),
   #
   #  ])
   #  def setup_class(self, summary):
   #      response = request.create_issue(JsonGenerator.create_issue(summary))
   #      response.status_code == 201
   #      self.id_issue.append(response.json().get("key"))


    # with  with missing required fields## with parameter text length longer than supported
    @pytest.mark.parametrize("summary, error_message", [
        ('', "You must specify a summary of the issue."),
        ('Serg'*25, "Summary must be less than 255 characters.")])
    def test_create_issue_incorrect_summary(self, summary, error_message):
        issue = IssuePage(self.driver)
        message = issue.create_incorrect_issue(summary)
        assert (error_message == message.gettext())

    ## with all required fields#
    def test_create_issue(self, summary="Serg_Summary4"):
        issue = IssuePage(self.driver)
        issue.create_issue(summary)



    # find one issue find 5  issues 
    @pytest.mark.parametrize("summary, search_result", [
        ('summary ~Serg_Summary4', 1),
        ('summary ~ Serg', 4),
        ('summary ~ Serg1111', 0),
    ])
    def test_search_issue(self, summary, search_result):
        issue = IssuePage(self.driver)
        assert (issue.search_issue() == search_result)

    def test_update_issue(self):
        pass


