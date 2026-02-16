from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models import Subject, Instructor
from app.schemas.subject_schema import (
    SubjectCreate,
    SubjectResponse,
)
from app.security import require_role, get_current_user



router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


@router.post("/", response_model=SubjectResponse)
def create_subject(
    subject: SubjectCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):

    # Check if instructor exists
    instructor = db.query(Instructor).filter(
        Instructor.id == subject.instructor_id
    ).first()

    if not instructor:
        raise HTTPException(
            status_code=404,
            detail="Instructor not found"
        )

    db_subject = Subject(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject


@router.get("/", response_model=List[SubjectResponse])
def get_subjects(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return db.query(Subject).all()




@router.get("/{subject_id}", response_model=SubjectResponse)
def get_subject(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    subject = db.query(Subject).filter(
        Subject.id == subject_id
    ).first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    return subject


@router.put("/{subject_id}", response_model=SubjectResponse)
def update_subject(
    subject_id: int,
    subject_data: SubjectCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    subject = db.query(Subject).filter(
        Subject.id == subject_id
    ).first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    # Check instructor exists
    instructor = db.query(Instructor).filter(
        Instructor.id == subject_data.instructor_id
    ).first()

    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")

    for key, value in subject_data.dict().items():
        setattr(subject, key, value)

    db.commit()
    db.refresh(subject)

    return subject


@router.delete("/{subject_id}")
def delete_subject(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    subject = db.query(Subject).filter(
        Subject.id == subject_id
    ).first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    db.delete(subject)
    db.commit()

    return {"message": "Subject deleted successfully"}


@router.get("/instructor/{instructor_id}", response_model=List[SubjectResponse])
def get_subjects_by_instructor(
    instructor_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return db.query(Subject).filter(
        Subject.instructor_id == instructor_id
    ).all()
