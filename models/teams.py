from pydantic import BaseModel


class Team(BaseModel):
    id: str
    owner_id: str
    path: str
    name: str
    logo: str
    description: str
    visibility: str
    created_at: int
