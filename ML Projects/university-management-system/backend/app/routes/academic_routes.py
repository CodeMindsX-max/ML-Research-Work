from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict

from app.database.db import get_db
from app.models import Enrollment, Subject

router = APIRouter(
    prefix="/academic",
    tags=["Academic Analytics"]
)

GRADE_POINTS = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0,
}


@router.get("/gpa/{student_id}/{semester}")
def calculate_semester_gpa(
    student_id: int,
    semester: int,
    db: Session = Depends(get_db)
):
    enrollments = db.query(Enrollment).filter(
        Enrollment.student_id == student_id,
        Enrollment.semester == semester
    ).all()

    if not enrollments:
        raise HTTPException(status_code=404, detail="No enrollments found")

    total_points = 0
    total_credits = 0

    for enrollment in enrollments:
        if enrollment.grade not in GRADE_POINTS:
            continue

        subject = db.query(Subject).filter(
            Subject.id == enrollment.subject_id
        ).first()

        if not subject:
            continue

        grade_point = GRADE_POINTS[enrollment.grade]
        total_points += grade_point * subject.credit_hours
        total_credits += subject.credit_hours

    if total_credits == 0:
        raise HTTPException(status_code=400, detail="No valid grades")

    gpa = total_points / total_credits

    return {
        "student_id": student_id,
        "semester": semester,
        "gpa": round(gpa, 2)
    }


@router.get("/cgpa/{student_id}")
def calculate_cgpa(student_id: int, db: Session = Depends(get_db)):
    enrollments = db.query(Enrollment).filter(
        Enrollment.student_id == student_id
    ).all()

    if not enrollments:
        raise HTTPException(status_code=404, detail="No enrollments found")

    total_points = 0
    total_credits = 0

    for enrollment in enrollments:
        if enrollment.grade not in GRADE_POINTS:
            continue

        subject = db.query(Subject).filter(
            Subject.id == enrollment.subject_id
        ).first()

        if not subject:
            continue

        grade_point = GRADE_POINTS[enrollment.grade]
        total_points += grade_point * subject.credit_hours
        total_credits += subject.credit_hours

    if total_credits == 0:
        raise HTTPException(status_code=400, detail="No valid grades")

    cgpa = total_points / total_credits

    return {
        "student_id": student_id,
        "cgpa": round(cgpa, 2)
    }



@router.get("/completed-credits/{student_id}")
def completed_credits(student_id: int, db: Session = Depends(get_db)):
    enrollments = db.query(Enrollment).filter(
        Enrollment.student_id == student_id
    ).all()

    if not enrollments:
        raise HTTPException(status_code=404, detail="No enrollments found")

    total_credits = 0

    for enrollment in enrollments:
        if enrollment.grade == "F":
            continue

        subject = db.query(Subject).filter(
            Subject.id == enrollment.subject_id
        ).first()

        if subject:
            total_credits += subject.credit_hours

    return {
        "student_id": student_id,
        "completed_credit_hours": total_credits
    }


@router.get("/failed-subjects/{student_id}")
def failed_subjects(student_id: int, db: Session = Depends(get_db)):
    enrollments = db.query(Enrollment).filter(
        Enrollment.student_id == student_id,
        Enrollment.grade == "F"
    ).all()

    failed_list = []

    for enrollment in enrollments:
        subject = db.query(Subject).filter(
            Subject.id == enrollment.subject_id
        ).first()

        if subject:
            failed_list.append({
                "subject_id": subject.id,
                "subject_name": subject.name,
                "semester": enrollment.semester
            })

    return {
        "student_id": student_id,
        "failed_subjects": failed_list
    }


@router.get("/summary/{student_id}")
def academic_summary(student_id: int, db: Session = Depends(get_db)):

    enrollments = db.query(Enrollment).filter(
        Enrollment.student_id == student_id
    ).all()

    if not enrollments:
        raise HTTPException(status_code=404, detail="No enrollments found")

    total_points = 0
    total_credits = 0
    completed_credits = 0
    failed = []

    for enrollment in enrollments:

        subject = db.query(Subject).filter(
            Subject.id == enrollment.subject_id
        ).first()

        if not subject:
            continue

        if enrollment.grade in GRADE_POINTS:
            grade_point = GRADE_POINTS[enrollment.grade]
            total_points += grade_point * subject.credit_hours
            total_credits += subject.credit_hours

        if enrollment.grade != "F":
            completed_credits += subject.credit_hours
        else:
            failed.append(subject.name)

    cgpa = round(total_points / total_credits, 2) if total_credits > 0 else 0

    return {
        "student_id": student_id,
        "cgpa": cgpa,
        "completed_credit_hours": completed_credits,
        "failed_subjects": failed
    }
