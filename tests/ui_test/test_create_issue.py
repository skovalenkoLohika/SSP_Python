import pytest
from JsonGenerator import *
from request_api import Api
from pages.issuePage import IssuePage
request = Api()


@pytest.mark.usefixtures("driver_setup")
class TestIssues:

    id_issue =[]


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
    def test_create_issue(self,summary,error_message):
        issue = IssuePage(self.driver)
        message = issue.create_incorrect_issue(summary)

    ## with all required fields#
    def test_create_issue(self, summary="Serg_Summary4"):
        issue = IssuePage(self.driver)
        issue.create_issue(summary)



    # find one issue find 5  issues  find issue “no results”
    def test_search_issue(self):
        pass

    def test_update_issue(self):
        pass


