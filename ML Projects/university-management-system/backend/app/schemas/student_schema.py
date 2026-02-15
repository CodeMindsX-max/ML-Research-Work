from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    department: str
    admission_year: int


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    admission_year: int

    class Config:
        from_attributes = True
