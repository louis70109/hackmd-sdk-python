from typing import List, Optional
from pydantic import BaseModel, validator
from models.users import User


class Notes(BaseModel):
    id: str
    title: str
    tags: Optional[List[str]]
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

    @validator('read_permission', 'write_permission')
    def permission_check(cls, v):
        if v not in ['owner', 'signed_in', 'guest']:
            raise ValueError("Permission must be ['owner', 'signed_in', 'guest']")
        return v

class Note(Notes):
    content: str


class NoteCreate(BaseModel):
    title: str
    content: str
    read_permission: str
    write_permission: str
    comment_permission: str

    @validator('read_permission', 'write_permission')
    def permission_check(cls, v):
        if v not in ['owner', 'signed_in', 'guest']:
            raise ValueError("Permission must be ['owner', 'signed_in', 'guest']")
        return v

    @validator('comment_permission')
    def comment_permission_check(cls, v):
        if v not in ['disabled', 'forbidden', 'owners', 'signed_in_users', 'everyone']:
            raise ValueError(
                "Comment permission must be ['disabled', 'forbidden', 'owners', 'signed_in_users', 'everyone']")
        return v


class NoteUpdate(BaseModel):
    content: str
    read_permission: str
    write_permission: str
    permalink: str

    @validator('read_permission', 'write_permission')
    def permission_check(cls, v):
        if v not in ['owner', 'signed_in', 'guest']:
            raise ValueError("Permission must be ['owner', 'signed_in', 'guest']")
        return v
