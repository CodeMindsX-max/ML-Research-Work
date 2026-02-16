from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models import Enrollment, Student, Subject
from app.schemas.enrollment_schema import (
    EnrollmentCreate,
    EnrollmentResponse, 
    EnrollmentUpdate
)

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)

def calculate_total(mid, final, internal):
    return (mid or 0) + (final or 0) + (internal or 0)


def calculate_grade(total):
    if total >= 85:
        return "A", 4.0
    elif total >= 75:
        return "B", 3.0
    elif total >= 65:
        return "C", 2.0
    elif total >= 50:
        return "D", 1.0
    else:
        return "F", 0.0


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


@router.get("/student/{student_id}/gpa")
def calculate_student_gpa(student_id: int, db: Session = Depends(get_db)):

    # Check student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    enrollments = db.query(Enrollment).filter(
        Enrollment.student_id == student_id,
        Enrollment.status == "active"  # or "completed" if you prefer
    ).all()

    if not enrollments:
        return {
            "student_id": student_id,
            "gpa": 0.0,
            "message": "No enrollments found"
        }

    total_quality_points = 0
    total_credit_hours = 0

    for enrollment in enrollments:
        if enrollment.grade_points is not None:
            credit_hours = enrollment.subject.credit_hours
            total_quality_points += enrollment.grade_points * credit_hours
            total_credit_hours += credit_hours

    if total_credit_hours == 0:
        return {
            "student_id": student_id,
            "gpa": 0.0,
            "message": "No graded subjects yet"
        }

    gpa = total_quality_points / total_credit_hours

    return {
        "student_id": student_id,
        "gpa": round(gpa, 2),
        "total_credit_hours": total_credit_hours
    }





#Get All Enrollments of a Student
@router.get("/student/{student_id}", response_model=List[EnrollmentResponse])
def get_student_enrollments(student_id: int, db: Session = Depends(get_db)):

    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return db.query(Enrollment).filter(
        Enrollment.student_id == student_id
    ).all()



#Get All Students in a Subject
@router.get("/subject/{subject_id}", response_model=List[EnrollmentResponse])
def get_subject_enrollments(subject_id: int, db: Session = Depends(get_db)):

    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    return db.query(Enrollment).filter(
        Enrollment.subject_id == subject_id
    ).all()


#Update Enrollment (Grade / Status)
@router.put("/{enrollment_id}", response_model=EnrollmentResponse)
def update_enrollment(
    enrollment_id: int,
    updated_data: EnrollmentUpdate,
    db: Session = Depends(get_db)
):

    enrollment = db.query(Enrollment).filter(
        Enrollment.id == enrollment_id
    ).first()

    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(enrollment, key, value)

    # Automatically calculate total, grade and grade points
    total = calculate_total(
        enrollment.mid_marks,
        enrollment.final_marks,
        enrollment.internal_marks
    )

    grade, points = calculate_grade(total)

    enrollment.total_marks = total
    enrollment.grade = grade
    enrollment.grade_points = points


    db.commit()
    db.refresh(enrollment)

    return enrollment



#Delete Enrollment (Drop Course)
@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):

    enrollment = db.query(Enrollment).filter(
        Enrollment.id == enrollment_id
    ).first()

    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    db.delete(enrollment)
    db.commit()

    return {"message": "Enrollment deleted successfully"}



#Filter by Semester (Very Realistic Feature)
@router.get("/semester/{semester}", response_model=List[EnrollmentResponse])
def get_enrollments_by_semester(semester: int, db: Session = Depends(get_db)):

    return db.query(Enrollment).filter(
        Enrollment.semester == semester
    ).all()


#Get Single Enrollment
@router.get("/{enrollment_id}", response_model=EnrollmentResponse)
def get_enrollment(enrollment_id: int, db: Session = Depends(get_db)):

    enrollment = db.query(Enrollment).filter(
        Enrollment.id == enrollment_id
    ).first()

    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    return enrollment



