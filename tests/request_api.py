import requests
from tests.variables import *

class Api:
    # credentials:
    HEADER = {'Authorization': 'Basic S292YWxlbmtvX1NlcmdleTpLb3ZAbGVua282==',
              'Content-Type': 'application/json'}

    # URLs:
    issue_url = 'http://jira.hillel.it:8080/rest/api/2/issue/'
    search_issue_url = 'http://jira.hillel.it:8080/rest/api/2/search?jql='

    def create_issue(self, json_data):
        response = requests.post(self.issue_url, headers=self.HEADER, data=json_data)
        return response

    def delete_issue(self, issue_id):
        response = requests.delete(self.issue_url + issue_id, headers=self.HEADER)
        if response.status_code == 204:
            print('isuue was successful deleted')
        else:
            print('Status code:' + str(response.status_code)+str(response.text))

    def login(self, user_name, password):
        response = requests.get(self.search_issue_url, auth=(user_name, password))
        return response.status_code

    def search_issue(self, search_parameters):
        response = requests.get(self.search_issue_url + search_parameters, auth=(USER_NAME, PASSWORD))
        return response

    def update_issue(self, issue_id, json_data):
        response = requests.put(self.issue_url+issue_id, headers=self.HEADER, data=json_data)
        return response

