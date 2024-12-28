import os

from github import Github

from core.args import parse_args
from core.repo import PydanticRepositoryState

args = parse_args()

token = os.getenv("GITHUB_TOKEN")
username = args.github_username
pull_request_number = args.pull_request_number

repo_state = PydanticRepositoryState.from_json_file(filename="repo_states.json")

github_client = Github(token)
star_to_review = github_client.get_repo(f"{username}/star-to-review")

pull_requests = star_to_review.get_pull(pull_request_number)

for repo in repo_state.repos:
    if repo.full_name in pull_requests.title and repo.state.PENDING.is_active:
        repo.state.cycle()

repo_state.save_to_json_file(filename="repo_states.json")
