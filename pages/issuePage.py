from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

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
    _searching_process = (By.CSS_SELECTOR, "div[class=loading]")
    _issue_created = (By.CSS_SELECTOR, "a[class^=issue-created]")
    _issue_summary = (By.ID, "summary-val")
    _issue_priority = (By.ID, "priority-val")
    _issue_assigner = (By.ID, "assignee-val")
    _cancel_button = (By.CSS_SELECTOR, "a[class='cancel']")
    _two_elements = (By.CSS_SELECTOR, "a[class^=issue-created], div[class=error]")
    _create_issue_dialog = (By.ID, "create-issue-dialog")

    def create_issue(self, summary):
        self.click_when_clickable(self._create_button)
        self.wait_for_visible(self._summary_field).send_keys(summary)
        self.click_when_clickable(self._create_issue_submit)
        message = self.wait_for_visible(self._two_elements)
        message_attrs = {'text': message.text, 'data-issue-key': message.get_attribute('data-issue-key')}
        if message.get_attribute('class') == 'error':
            self.click_when_clickable(self._cancel_button)
            self.wait_for_alert()
            alert = self.driver.switch_to.alert
            alert.accept()
            sleep(1)
        return message_attrs

    def search_issue(self, search_parameter):
        self.click_when_clickable(self._issue_button)
        self.click_when_clickable(self._search_for_issues)
        self.wait_for_visible(self._advanced_search_field).clear().send_keys(search_parameter).send_keys(Keys.ENTER)
        self.wait_for_invisible(self._searching_process)
        return self.wait_for_visible_elements(self._issue_list).count()

    def update_issue(self, issue, summary="summary", priority="High", assigner="Kovalenko Sergey"):
        result = []
        self.search_issue(issue)
        self.wait_for_visible_elements(self._issue_list)
        self.wait_for_visible(self._issue_summary).clear().send_keys(summary)
        self.wait_for_visible(self._issue_priority).clear().send_keys(priority)
        self.wait_for_visible(self._issue_assigner).clear().\
            send_keys(assigner).send_keys(Keys.ENTER).send_keys(Keys.ENTER)
        self.search_issue(issue)
        self.wait_for_visible_elements(self._issue_list)
        result.append(self.wait_for_visible(self._issue_summary).text)
        result.append(self.wait_for_visible(self._issue_priority).text)
        result.append(self.wait_for_visible(self._issue_assigner).text)
        return result













