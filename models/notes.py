import datetime
from typing import List, Optional
from pydantic import BaseModel
from datetime import date

from models.users import User


class Notes(BaseModel):
    id: str
    title: str
    tags: List[str]
    created_at: int
    publish_type: str
    published_at: Optional[int] = None
    permalink: Optional[str] = None
    short_id: str
    last_changed_at: int
    last_change_user: User
    user_path: str
    team_path: Optional[str] = None
    read_permission: str
    write_permission: str
    publish_link: str


class Note(Notes):
    content: str
