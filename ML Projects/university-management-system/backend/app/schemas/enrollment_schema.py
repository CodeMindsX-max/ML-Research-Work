from pydantic import BaseModel
from typing import Optional


class EnrollmentBase(BaseModel):
    student_id: int
    subject_id: int
    semester: int

    mid_marks: Optional[float] = 0
    final_marks: Optional[float] = 0
    internal_marks: Optional[float] = 0

    grade: Optional[str] = None
    grade_points: Optional[float] = None
    status: Optional[str] = "active"



class EnrollmentCreate(EnrollmentBase):
    pass


class EnrollmentResponse(EnrollmentBase):
    id: int

    class Config:
        from_attributes = True


class EnrollmentUpdate(BaseModel):
    mid_marks: Optional[float] = None
    final_marks: Optional[float] = None
    internal_marks: Optional[float] = None
    status: Optional[str] = None

