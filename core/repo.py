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

    @field_serializer("last_commit")
    def serialize_last_commit(self, dt: datetime.datetime):
        return dt.isoformat()

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
    repos: dict[str, PydanticRepository] = Field(default_factory=dict)

    @classmethod
    def from_json_file(cls, filename: str):
        if os.path.exists(filename):
            with open(filename) as f:
                data = json.load(f)
                # 多重解析巢狀 JSON 字串
                while isinstance(data, str):
                    data = json.loads(data)
                
                # 處理最舊版直接儲存 list 的格式
                if isinstance(data, list):
                    return cls(repos={r.full_name: r for r in [PydanticRepository(**item) for item in data]})
                
                # 兼容過渡版 list 格式 (包含在 "repos" key 中)
                repos_data = data.get("repos", [])
                if isinstance(repos_data, list):
                    return cls(repos={r.full_name: r for r in [PydanticRepository(**item) for item in repos_data]})
                
                # 處理新版 dict 格式
                return cls(repos={k: PydanticRepository(**v) for k, v in data.get("repos", {}).items()})
        return cls()

    def save_to_json_file(self, filename: str):
        with open(filename, "w") as f:
            json.dump({"repos": {k: v.model_dump(mode="json") for k, v in self.repos.items()}}, f, indent=2)

    def add(self, repo: PydanticRepository):
        """Add repository only if not exists"""
        if repo.full_name not in self.repos:
            self.repos[repo.full_name] = repo


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

    for repo in repo_state.repos.values():

        if repo.full_name in [repo.full_name for repo in repos]:
            print(f"Repository {repo.full_name} already exists in state.")
            continue

        print(f"Adding repository {repo.full_name} to state.")
        
        r = PydanticRepository.from_repo(repo)
        repo_state.add(r)

    repo_state.save_to_json_file(filename="repo_states.json")
