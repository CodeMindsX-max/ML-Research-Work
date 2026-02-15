from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models import Instructor
from app.schemas.instructor_schema import (
    InstructorCreate,
    InstructorResponse,
)

router = APIRouter(
    prefix="/instructors",
    tags=["Instructors"]
)


@router.post("/", response_model=InstructorResponse)
def create_instructor(
    instructor: InstructorCreate,
    db: Session = Depends(get_db)
):
    db_instructor = Instructor(**instructor.dict())
    db.add(db_instructor)
    db.commit()
    db.refresh(db_instructor)
    return db_instructor


@router.get("/", response_model=List[InstructorResponse])
def get_instructors(db: Session = Depends(get_db)):
    return db.query(Instructor).all()


@router.get("/{instructor_id}", response_model=InstructorResponse)
def get_instructor(instructor_id: int, db: Session = Depends(get_db)):
    instructor = db.query(Instructor).filter(
        Instructor.id == instructor_id
    ).first()

    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")

    return instructor
