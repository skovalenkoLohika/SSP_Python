import json


class JsonGenerator:

    @staticmethod
    def create_issue(self, summary_id=""):
        jira = \
            {"fields": {
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
    def update_issue(self, description="new summary form K"):
        jira = {
            "update": {
                "description": [
                    {
                        "set": description
                    }
                ],
                "comment": [
                    {
                        "add": {
                            "body": "Body"}}]}}
