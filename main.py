from collections import Counter
from typing import cast

from jira import JIRA
from jira.client import ResultList
from jira.resources import Issue

USER = ""
PWD = ""

id_done= "31"
# Some Authentication Methods
jira = JIRA(
    basic_auth=(USER, PWD),  # a username/password tuple [Not recommended]
    # basic_auth=("email", "API token"),  # Jira Cloud: a username/token tuple
    # token_auth="API token",  # Self-Hosted Jira (e.g. Server): the PAT token
    # auth=("admin", "admin"),  # a username/password tuple for cookie auth [Not recommended]
    server="https://jira.arkeup.com/"
)

def update_to_done(issu_list=[]):
    for issue in issu_list:
        name = issue.key
        jira.transition_issue(name, id_done)
        print(f"MAJ: {name} OK")
        break

if __name__ == "__main__":
    all = jira.search_issues('project = F2F AND status in ("En attente de validation", "In Progress", "To Do") AND assignee in (currentUser())')
    print(f"Found {len(all)} tickets")
    update_to_done(all)