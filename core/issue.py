from typing import List

from core.repo import PydanticRepository
from github import Repository
from jinja2 import Template

with open("core/review.template.md") as f:
    review_template = Template(f.read())


def create_issue(star_to_review: Repository, repo: PydanticRepository, assignees: List[str] = []) -> None:
    title = "Daily Review: `{}`".format(repo.full_name)
    body = review_template.render(repo=repo)
    labels = ["daily_review"]

    if "awesome" in repo.full_name.lower():
        labels.append("awesome")

    return star_to_review.create_issue(
        title=title,
        body=body,
        assignees=assignees,
        labels=labels,
    )


if __name__ == "__main__":
    import os

    from args import parse_args
    from dotenv import load_dotenv

    load_dotenv()

    args = parse_args()
    token = os.getenv("GITHUB_TOKEN")
    username = args.github_username

    from repo import PydanticRepositoryState

    repo_state = PydanticRepositoryState.from_json_file(filename="repo_states.json")

    for repo in repo_state.repos[4:]:
        create_issue(repo)
        break
