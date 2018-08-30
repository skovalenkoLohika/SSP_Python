import requests


class Api:
    # credentials:
    USER_NAME = 'Kovalenko_Sergey'
    PASSWORD = 'Kov@lenko6'
    HEADER = {'Authorization': 'Basic S292YWxlbmtvX1NlcmdleTpLb3ZAbGVua282==', 'Content-Type': 'application/json'}

    # URLs:
    create_issue_url = 'http://jira.hillel.it:8080/rest/api/2/issue'
    search_issue_url = 'http://jira.hillel.it:8080/rest/api/2/search?jql='
    update_issue_url = 'http://jira.hillel.it:8080/rest/api/2/issue/'

    def create_issue(self, json_data):
        r = requests.post(self.create_issue_url, headers=self.HEADER, data=json_data)
        if r.status_code == 201:
            print('isuue was successful created')
            return [r.status_code, r.json().get("id")]
        else:
            print('Status code:' + str(r.status_code)+str(r.text))

    def login(self, user_name, password):
        r = requests.get(self.search_issue_url, auth=(user_name, password))
        return r.status_code

    # def search_issue(self, search_parameters):
    #     r = requests.get(create_issue_url + search_parameters, auth=(USER_NAME, PASSWORD))

    def update_issue(self, issue_id,json_data):
        r = requests.put(self.update_issue_url+issue_id, headers=self.HEADER, data=json_data)
