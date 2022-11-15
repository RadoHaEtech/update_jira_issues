from collections import Counter
from typing import cast

from jira import JIRA
from jira.client import ResultList
from jira.resources import Issue

user = ""
pwd = ""
# Some Authentication Methods
jira = JIRA(
    basic_auth=(user, pwd),  # a username/password tuple [Not recommended]
    # basic_auth=("email", "API token"),  # Jira Cloud: a username/token tuple
    # token_auth="API token",  # Self-Hosted Jira (e.g. Server): the PAT token
    # auth=("admin", "admin"),  # a username/password tuple for cookie auth [Not recommended]
    server="https://jira.arkeup.com/"
)
jira.search_issues('project = F2F AND status in ("En attente de validation", "In Progress", "To Do") AND assignee in (currentUser())')
if __name__ == "__main__":
    myself = jira.myself()
    issues = cast(ResultList[Issue], jira.search_issues("assignee=me"))
    print(issues)