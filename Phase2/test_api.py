import pytest
from .request_api import *
from .JsonGenerator import *

request = Api()


class TestApi:
    USER_NAME = 'Kovalenko_Sergey'
    PASSWORD = 'Kov@lenko6'
    WRONG_USER = 'Kovalenko_S'
    WRONG_PASSWORD = 'KovalenkoS'
    id_issue =[]

    @pytest.mark.parametrize("user_name,password, expected_code", [
        (USER_NAME, PASSWORD, 200),
        (PASSWORD, WRONG_USER, 401),
        (WRONG_PASSWORD, PASSWORD, 401),
    ])
    def test_login(self, user_name, password, expected_code):
        assert request.login(user_name, password) == expected_code

    # Create 5 Issues
    def test_create_issue(self):
        response = request.create_issue(JsonGenerator.create_issue(self, "summary"))
        try:
            self.id_issue.append(response.json().get("key"))
        except AttributeError:
            assert

    def test_update_issue(self):
        response = request.create_issue(JsonGenerator.create_issue(self))
        self.id_issue = response.json().get("key")

