from pydantic import BaseModel, EmailStr
from typing import List, Optional


class InstructorBase(BaseModel):
    name: str
    email: EmailStr


class InstructorCreate(InstructorBase):
    pass


class InstructorResponse(InstructorBase):
    id: int

    class Config:
        from_attributes = True
