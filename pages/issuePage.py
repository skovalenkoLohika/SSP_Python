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


    def create_issue(self, summary):

        self.click_when_clickable(self.create_button)
        self.wait_for_visible(self.summary_field)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=summary]").




