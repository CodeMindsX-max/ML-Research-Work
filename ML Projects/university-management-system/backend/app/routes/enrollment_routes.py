from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models import Enrollment, Student, Subject
from app.schemas.enrollment_schema import (
    EnrollmentCreate,
    EnrollmentResponse,
)

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


@router.post("/", response_model=EnrollmentResponse)
def enroll_student(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):

    # Check student exists
    student = db.query(Student).filter(
        Student.id == enrollment.student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check subject exists
    subject = db.query(Subject).filter(
        Subject.id == enrollment.subject_id
    ).first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    # Optional: Prevent duplicate enrollment
    existing = db.query(Enrollment).filter(
        Enrollment.student_id == enrollment.student_id,
        Enrollment.subject_id == enrollment.subject_id,
        Enrollment.semester == enrollment.semester
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Student already enrolled in this subject for this semester"
        )

    db_enrollment = Enrollment(**enrollment.dict())
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)

    return db_enrollment


@router.get("/", response_model=List[EnrollmentResponse])
def get_enrollments(db: Session = Depends(get_db)):
    return db.query(Enrollment).all()
