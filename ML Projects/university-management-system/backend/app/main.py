import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.database.db import engine, Base
from app.models import Student, Instructor, Subject, Enrollment
from app.routes.student_routes import router as student_router

load_dotenv()

app = FastAPI(title=os.getenv("PROJECT_NAME"))

Base.metadata.create_all(bind=engine)

app.include_router(student_router)

@app.get("/")
def root():
    return {"message": "Student API Ready"}
