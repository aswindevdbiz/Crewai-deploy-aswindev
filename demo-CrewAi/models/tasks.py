from typing import List
from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str | None = None
    outcome: str
    agents: list[str]
    tasks: list[str]
    image: str
    active: bool = True

    