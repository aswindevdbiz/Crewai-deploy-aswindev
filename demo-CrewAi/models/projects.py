from typing import List
from pydantic import BaseModel


class Project(BaseModel):
    name: str
    description: str | None = None
    crews: list[str]
    active: bool = True
