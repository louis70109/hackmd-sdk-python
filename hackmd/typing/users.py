from typing import List, Optional
from pydantic import BaseModel

from hackmd.typing.teams import Team


class UserBase(BaseModel):
    name: str
    photo: str
    user_path: str


class Me(UserBase):
    id: str
    email: Optional[str] = None
    teams: List[Team]


class User(UserBase):
    biography: Optional[str] = None
