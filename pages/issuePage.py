from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base import Base


class IssuePage(Base):

    _create_button = (By.ID, "create_link")
    _summary_field = (By.CSS_SELECTOR, "input[name=summary]")
    _create_issue_submit = (By.ID, "create-issue-submit")
    _assignee = (By.ID, "assignee-field")
    _priority = (By.ID, "priority-field")
    _error_message = (By.CSS_SELECTOR, "div[class=error]")
    _issue_button = (By.ID, "find_link")
    _search_for_issues = (By.CLASS_NAME, "Search for issues")
    _advanced_search_field = (By.ID, "advanced-search")
    _issue_list = (By.CSS_SELECTOR, "li[title]")
    _searching_process =(By.CSS_SELECTOR, "div[class=loading]")
    _issue_created = (By.CSS_SELECTOR, "a[class^=issue-created]")

    def create_issue(self, summary):
        self.click_when_clickable(self._create_button)
        self.wait_for_visible(self._summary_field).send_keys(summary)
        self.click_when_clickable(self._create_issue_submit)
        try:
            self.wait_for_visible(self._issue_created)
            return self.driver.find_element(self._issue_created).text
        except TimeoutException:
            ttt = self.driver.find_element(self._error_message).text
            return ttt




    # def create_incorrect_issue(self, summary):
    #     self.click_when_clickable(self._create_button)
    #     self.wait_for_visible(self._summary_field).send_keys(summary)
    #     self.click_when_clickable(self._create_issue_submit)
    #     return self.wait_for_visible(self._error_message)

    def search_issue(self, search_parameter):
        self.click_when_clickable(self._issue_button)
        self.click_when_clickable(self._search_for_issues)
        self.wait_for_visible(self._advanced_search_field).clear().send_keys(search_parameter).send_keys(Keys.ENTER)
        self.wait_for_invisible(self._searching_process)
        return self.driver.find_elements(self._issue_list).count()








