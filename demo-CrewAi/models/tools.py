from fastapi import UploadFile
from pydantic import BaseModel

class Tool(BaseModel):
    name: str 
    description: str | None = None
    image: str
    active: bool = True

    

