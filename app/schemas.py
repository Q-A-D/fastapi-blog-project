from pydantic import BaseModel
from typing import Optional

class AuthorBase(BaseModel):
    name: str
    email: str

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title: str
    content: str
    author_id: int

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    class Config:
        from_attributes = True
