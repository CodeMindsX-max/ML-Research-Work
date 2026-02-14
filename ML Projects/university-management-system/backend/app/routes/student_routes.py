from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.models.student import Student

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students")
def create_student(student: dict, db: Session = Depends(get_db)):
    db_student = Student(**student)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
