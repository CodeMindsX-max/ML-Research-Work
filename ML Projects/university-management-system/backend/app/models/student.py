from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    department = Column(String)
    admission_year = Column(Integer)


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    course_id = Column(Integer)
    semester_id = Column(Integer)
    instructor_id = Column(Integer)
    grade = Column(String)
