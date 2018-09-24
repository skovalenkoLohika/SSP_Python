from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from tests.base import Base


class IssuePage(Base):

    _create_button = (By.ID, "create_link")
    _summary_field = (By.CSS_SELECTOR, "input[name=summary]")
    _create_issue_submit = (By.ID, "create-issue-submit")
    _assignee = (By.ID, "assignee-field")
    _assignee_field =(By.CSS_SELECTOR, "input[id=assignee-field]")
    _assignee_suggestion =(By.CSS_SELECTOR, "input[aria-expanded=true]")
    _priority = (By.ID, "priority-field")
    _priority_field = (By.CSS_SELECTOR, "input[id=priority-field]")
    _error_message = (By.CSS_SELECTOR, "div[class=error]")
    _issue_button = (By.ID, "find_link")
    _search_for_issues = (By.ID, "issues_new_search_link_lnk")
    _advanced_search_field = (By.ID, "advanced-search")
    _issue_list = (By.CLASS_NAME, "issue-list")
    _search_result = (By.CSS_SELECTOR, "p[class=no-results-hint], ol[class=issue-list]")
    _searching_process = (By.CSS_SELECTOR, "div[class=loading]")
    _issue_created = (By.CSS_SELECTOR, "a[class^=issue-created]")
    _issue_summary = (By.ID, "summary-val")
    _issue_input =(By.ID, "summary")
    _issue_priority = (By.ID, "priority-val")
    _issue_assignee = (By.ID, "assignee-val")
    _cancel_button = (By.CSS_SELECTOR, "a[class='cancel']")
    _two_elements = (By.CSS_SELECTOR, "a[class^=issue-created], div[class=error]")
    _create_issue_dialog = (By.ID, "create-issue-dialog")
    _dropdawn_menu = (By.ID, "issues_new")
    _conteins_text_search = (By.CSS_SELECTOR, "input[class^=search-entry]")

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
        else:
            self.wait_for_visible(self._issue_created)
            self.wait_for_invisible(self._issue_created)
        return message_attrs

    def search_issue(self, search_parameter):
        self.click_when_clickable(self._issue_button)
        self.wait_for_visible(self._dropdawn_menu)
        self.click_when_clickable(self._search_for_issues)
        search_field = self.wait_for_when_clickable(self._conteins_text_search)
        search_field.send_keys(search_parameter)
        search_field.send_keys(Keys.ENTER)
        sleep(2)
        self.wait_for_invisible(self._searching_process)
        result = self.wait_for_visible(self._search_result)
        if result.get_attribute('class') == 'no-results-hint':
            return 0
        else:
            return len(result.find_elements_by_tag_name("li"))

    def update_issue(self, issue, summary="summary", priority="High", assigner="Kovalenko Sergey"):
        result = []
        self.search_issue(issue)
        self.wait_for_visible_elements(self._issue_list)
        self.click_when_clickable(self._issue_summary)
        summary_field = self.wait_for_when_clickable(self._issue_input)
        summary_field.clear()
        summary_field.send_keys(summary)
        summary_field.send_keys(Keys.ENTER)
        self.click_when_clickable(self._issue_priority)
        self.wait_for_visible(self._priority_field)
        priority_field = self.wait_for_when_clickable(self._priority_field)
        priority_field.click()
        priority_field.clear()
        priority_field.send_keys(priority)
        priority_field.send_keys(Keys.ENTER)
        self.click_when_clickable(self._issue_assignee)
        assignee_field = self.wait_for_when_clickable(self._assignee_field)
        assignee_field.clear()
        assignee_field.send_keys(assigner)
        self.wait_for_visible(self._assignee_suggestion)
        assignee_field.send_keys(Keys.ENTER)
        assignee_field.send_keys(Keys.ENTER)
        self.search_issue(summary)
        result.append(self.wait_for_visible(self._issue_summary).text)
        result.append(self.wait_for_visible(self._issue_priority).text)
        result.append(self.wait_for_visible(self._issue_assignee).text)
        return result













