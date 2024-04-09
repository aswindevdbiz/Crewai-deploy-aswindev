from typing import List
from pydantic import BaseModel


class Agent(BaseModel):
    role: str
    goal: str
    backstory: str | None = None
    tools: List[str]
    verbose: bool 
    image: str
    active: bool = True

    