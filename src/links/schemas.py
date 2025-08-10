from pydantic import BaseModel


class NewLink(BaseModel):
    content: str
    