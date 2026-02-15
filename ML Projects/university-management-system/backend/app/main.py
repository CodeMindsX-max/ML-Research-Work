import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.database.db import engine, Base
from app.models import Student, Instructor, Subject, Enrollment
from app.routes.student_routes import router as student_router
from app.routes.instructor_routes import router as instructor_router
from app.routes.subject_routes import router as subject_router
from app.routes.enrollment_routes import router as enrollment_router
from app.routes.academic_routes import router as academic_router





load_dotenv()

app = FastAPI(title=os.getenv("PROJECT_NAME"))

Base.metadata.create_all(bind=engine)

app.include_router(student_router)
app.include_router(instructor_router)
app.include_router(subject_router)
app.include_router(enrollment_router)
app.include_router(academic_router)



@app.get("/")
def root():
    return {"message": "Student API Ready"}
