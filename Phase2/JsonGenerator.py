import json


class JsonGenerator:

    @staticmethod
    def create_issue(summary_id=''):
        jira = {"fields": {
                "project":
                    {
                        "key": "AQAPYTHON"
                    },
                "summary": summary_id,
                "description": "random_desc",
                "issuetype": {
                    "name": "Bug"
                }}}
        return json.dumps(jira)

    @staticmethod
    def update_issue(field, value):
        jira = {"fields": {field: value}}
        return json.dumps(jira)

