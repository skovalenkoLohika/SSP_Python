from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from base import Base


class IssuePage(Base):

    create_button = (By.ID, "create_link")
    summary_field = (By.CSS_SELECTOR, "input[name=summary]")
    create_issue = (By.ID, "create-issue-submit")
    assignee = (By.ID, "assignee-field")
    priority = (By.ID, "priority-field")
    error_message = (By.CSS_SELECTOR, "div[class=error]")

    def create_issue(self, summary):
        self.click_when_clickable(self.create_button)
        self.wait_for_visible(self.summary_field).send_keys(summary)

    def create_incorrect_issue(self, summary):
        self.click_when_clickable(self.create_button)
        self.wait_for_visible(self.summary_field).send_keys(summary)
        return self.wait_for_visible(self.error_message)




