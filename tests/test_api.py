import pytest
from tests.request_api import Api
from tests.JsonGenerator import *
from tests.variables import *

request = Api()


@pytest.mark.api
class TestApi:

    id_issue = []
    i = 1
    summary = ['Serg_Summary1', 'Serg_Summary2']

    def setup_class(self):
        for i in self.summary:
            response = request.create_issue(JsonGenerator.create_issue(i))
            if response.status_code == 201:
                self.id_issue.append(response.json().get("key"))
                print("Issue created" + response.json().get("key"))

    def teardown_class(self):
        if len(self.id_issue) > 0:
            for i in self.id_issue:
                request.delete_issue(i)

    @pytest.mark.parametrize("user_name,password, expected_code", [
        (USER_NAME, PASSWORD, 200),
        (PASSWORD, WRONG_USER, 401),
        (WRONG_PASSWORD, PASSWORD, 401),
    ])
    def test_login(self, user_name, password, expected_code):
        assert expected_code == request.login(user_name, password)

    @pytest.mark.parametrize("summary, code", [
        ('Serg_Summary3', 201),
        ('', 400),
        ('summary' * 45, 400),
    ])
    def test_create_issue(self, summary, code):
        response = request.create_issue(JsonGenerator.create_issue(summary))
        assert response.status_code == code
        if code == 201:
            self.id_issue.append(response.json().get("key"))


    # search by id
    def test_search_issue(self):
        response = request.search_issue('id=' + self.id_issue[0])
        assert response.status_code == 200

    # search by absent id
    def test_search_issue(self):
        response = request.search_issue('id=12345678')
        assert response.status_code == 400

    # search by reporter
    def test_search_issue(self):
        response = request.search_issue('reporter=' + USER_NAME)
        assert response.status_code == 200
        assert 2 <= len(response.json().get("issues"))

    @pytest.mark.parametrize("field, value", [
        ('summary', 'Serg_new_summary'),
        ('description', 'Serg_new_description'),
    ])
    def test_update_issue(self, field, value):
        response = request.update_issue(self.id_issue[0], JsonGenerator.update_issue(field, value))
        assert 204 == response.status_code

    @pytest.mark.flaky(reruns=1)
    def test_rerun(self):
        try:
            assert 2 == TestApi.i
        finally:
            TestApi.i += 1


