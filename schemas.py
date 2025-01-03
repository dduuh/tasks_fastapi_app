from pydantic import BaseModel
from typing import Optional

class STaskAdd(BaseModel):
    name: str
    description: str

class STask(STaskAdd):
    id: int

class SUsersAdd(BaseModel):
    username: str
    password: str

class SUsers(SUsersAdd):
    id: int