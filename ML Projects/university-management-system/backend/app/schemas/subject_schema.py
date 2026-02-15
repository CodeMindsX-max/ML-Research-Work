from pydantic import BaseModel
from typing import Optional


class SubjectBase(BaseModel):
    name: str
    credit_hours: int
    instructor_id: int


class SubjectCreate(SubjectBase):
    pass


class SubjectResponse(SubjectBase):
    id: int

    class Config:
        from_attributes = True
