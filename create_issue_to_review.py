import os

from github import Github

from core.args import parse_args
from core.issue import create_issue
from core.repo import PydanticRepositoryState

args = parse_args()

token = os.getenv("GITHUB_TOKEN")
username = args.github_username

repo_state = PydanticRepositoryState.from_json_file(filename="repo_states.json")
github_client = Github(token)

star_to_review = github_client.get_repo(f"{username}/star-to-review")

for repo in repo_state.repos.values():
    if repo.state.UNREVIEWED.is_active:
        issue = create_issue(
            star_to_review=star_to_review, repo=repo, assignees=[username]
        )
        repo.state.to_pending()
        repo.issue_number = issue.number
        break

repo_state.save_to_json_file(filename="repo_states.json")
