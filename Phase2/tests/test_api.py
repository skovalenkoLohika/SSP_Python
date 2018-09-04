import pytest
from Phase2.api.request_api import Api
from Phase2.JsonGenerator import *

request = Api()


class TestApi:
    USER_NAME = 'Kovalenko_Sergey'
    PASSWORD = 'Kov@lenko6'
    WRONG_USER = 'Kovalenko_S'
    WRONG_PASSWORD = 'KovalenkoS'
    id_issue = []

    @pytest.mark.parametrize("user_name,password, expected_code", [
        (USER_NAME, PASSWORD, 200),
        (PASSWORD, WRONG_USER, 401),
        (WRONG_PASSWORD, PASSWORD, 401),
    ])
    def test_login(self, user_name, password, expected_code):
        assert expected_code == request.login(user_name, password)

    @pytest.mark.parametrize("summary, code", [
        ('Serg_Summary1', 201),
        ('Serg_Summary2', 201),
        ('Serg_Summary3', 201),
        ('', 400),
        ('summary' * 45, 400),
    ])
    def test_create_issue(self, summary, code):
        response = request.create_issue(JsonGenerator.create_issue(summary))
        assert response.status_code == code
        if code == 201:
            self.id_issue.append(response.json().get("key"))
        print(self.id_issue)

    # search by id
    @pytest.mark.dependsy(depends=["test_create_issue"])
    def test_search_issue(self):
        response = request.search_issue('id=' + self.id_issue[0])
        assert response.status_code == 200

    # search by absent id
    @pytest.mark.dependsy(depends=["test_create_issue"])
    def test_search_issue(self):
        response = request.search_issue('id=12345678')
        assert response.status_code == 400

    # search by reporter
    @pytest.mark.dependsy(depends=["test_create_issue"])
    def test_search_issue(self):
        response = request.search_issue('reporter=' + self.USER_NAME)
        assert response.status_code == 200
        assert 3 == len(response.json().get("issues"))


    @pytest.mark.parametrize("field, value", [
         ('summary', 'Serg_new_summary'),
         ('description', 'Serg_new_description'),
    ])
    @pytest.mark.dependsy(depends=["test_create_issue"])
    def test_update_issue(self, field, value):
        response = request.update_issue(self.id_issue[0], JsonGenerator.update_issue(field, value))
        assert 204 == response.status_code


    def teardown_class(self):
        if len(self.id_issue) > 0:
            for i in range(len(self.id_issue)):
                request.delete_issue(self.id_issue[i])

