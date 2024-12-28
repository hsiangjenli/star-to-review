import os

from github import Github

from core.args import parse_args
from core.repo import PydanticRepositoryState

args = parse_args()

token = os.getenv("GITHUB_TOKEN")
username = args.github_username

repo_state = PydanticRepositoryState.from_json_file(filename="repo_states.json")
github_client = Github(token)

star_to_review = github_client.get_repo(f"{username}/star-to-review")

for repo in repo_state.repos:
    if repo.state.REVIEWED.is_active:
        star_to_review.get_issue(repo.issue_number).edit(state="open")
        repo.state.cycle()

repo_state.save_to_json_file(filename="repo_states.json")
