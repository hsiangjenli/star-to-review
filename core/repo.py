import datetime
import json
import os
from typing import List, Optional

from github import Github, Repository
from pydantic import BaseModel, Field, field_serializer, field_validator
from statemachine import State, StateMachine


class ReviewState(StateMachine):
    UNREVIEWED = State("UNREVIEWED", initial=True)
    PENDING = State("PENDING")
    REVIEWED = State("REVIEWED")
    NO_PLAN = State("NO_PLAN")

    to_pending = UNREVIEWED.to(PENDING)
    to_reviewed = PENDING.to(REVIEWED)
    to_no_plan = PENDING.to(NO_PLAN)

    to_reconsider = REVIEWED.to(PENDING)
    to_reconsider_no_plan = NO_PLAN.to(PENDING)

    def before_cycle(self, event: str, source: State, target: State):
        print(f"Transitioning from {source} to {target}")


class PydanticRepository(BaseModel):
    name: str
    full_name: str
    html_url: str
    description: Optional[str]
    stargazers_count: int
    state: ReviewState = Field(default_factory=ReviewState)
    last_commit: datetime.datetime = Field(default_factory=datetime.datetime.now)
    issue_number: Optional[int] = Field(default=None)

    class Config:
        arbitrary_types_allowed = True  # 忽略自定義類型的模式生成

    @field_serializer("state")
    def serialize_state(self, state: ReviewState):
        return state.current_state.name

    @field_validator("state", mode="before")
    @classmethod
    def deserialize_state(cls, value: str) -> ReviewState:
        if isinstance(value, str):
            state_machine = ReviewState()
            setattr(state_machine, "current_state", getattr(ReviewState, value))
            return state_machine
        return value

    @classmethod
    def from_repo(cls, repo: Repository):
        return cls(
            name=repo.name,
            full_name=repo.full_name,
            html_url=repo.html_url,
            description=repo.description,
            stargazers_count=repo.stargazers_count,
            state=ReviewState(),
        )


class PydanticRepositoryState(BaseModel):
    repos: List[PydanticRepository] = []

    @classmethod
    def from_json_file(cls, filename: str):
        if os.path.exists(filename):
            with open(filename) as f:
                return cls.model_validate_json(json.load(f))
        return cls()

    def save_to_json_file(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.model_dump_json(), f)

    def add(self, repo: PydanticRepository):
        self.repos.append(repo)


def get_starred_repos(username: str, token: str) -> Repository:
    """

    Args:
        username (str): GitHub username
        token (str): GitHub token can be generated from Developer Settings

    Returns:
        Repository: Starred repositories
    """
    g = Github(token)
    user = g.get_user(username)
    repos = user.get_starred()
    return repos


if __name__ == "__main__":
    import os

    import dotenv
    from args import parse_args

    args = parse_args()

    dotenv.load_dotenv()

    token = os.getenv("GITHUB_TOKEN")
    username = args.github_username
    repos = get_starred_repos(username, token)

    repo_state = PydanticRepositoryState.from_json_file(filename="repo_states.json")

    for repo in repos:
        r = PydanticRepository.from_repo(repo)
        repo_state.add(r)

    repo_state.save_to_json_file(filename="repo_states.json")
