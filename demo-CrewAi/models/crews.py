from typing import List
from pydantic import BaseModel


class Crew(BaseModel):
    name: str
    description: str | None = None
    tasks: list[str]
    agents: list[str]
    image: str
    active: bool = True
    