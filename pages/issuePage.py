import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base import Base


class IssuePage(Base):

    create_button = (By.ID, "create_link")
    summary_field = (By.CSS_SELECTOR, "input[name=summary]")
    create_issue_submit = (By.ID, "create-issue-submit")
    assignee = (By.ID, "assignee-field")
    priority = (By.ID, "priority-field")
    error_message = (By.CSS_SELECTOR, "div[class=error]")
    issue_button = (By.ID, "find_link")
    search_for_issues = (By.CLASS_NAME, "Search for issues")
    advanced_search_field = (By.ID, "advanced-search")
    issue_list = (By.CLASS_NAME, "list-content")

    def create_issue(self, summary):
        self.click_when_clickable(self.create_button)
        self.wait_for_visible(self.summary_field).send_keys(summary)
        self.click_when_clickable(self.create_issue_submit)
        self.wait_for_invisible(self.summary_field)

    def create_incorrect_issue(self, summary):
        self.click_when_clickable(self.create_button)
        self.wait_for_visible(self.summary_field).send_keys(summary)
        self.click_when_clickable(self.create_issue_submit)
        return self.wait_for_visible(self.error_message)

    def search_issue(self, search_parameter):
        self.click_when_clickable(self.issue_button)
        self.click_when_clickable(self.search_for_issues)
        self.wait_for_invisible(self.advanced_search_field).send_keys(search_parameter).send_keys(Keys.ENTER)
        time.sleep(1)
        return self.wait_for_invisible(self.issue_list)








