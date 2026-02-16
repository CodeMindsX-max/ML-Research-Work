from pydantic import BaseModel
from typing import Optional


class EnrollmentBase(BaseModel):
    student_id: int
    subject_id: int
    semester: int
    grade: Optional[str] = None
    status: Optional[str] = None


class EnrollmentCreate(EnrollmentBase):
    pass


class EnrollmentResponse(EnrollmentBase):
    id: int

    class Config:
        from_attributes = True


class EnrollmentUpdate(BaseModel):
    grade: Optional[str] = None
    status: Optional[str] = None

