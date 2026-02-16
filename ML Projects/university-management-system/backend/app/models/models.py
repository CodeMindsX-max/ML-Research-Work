from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.database.db import Base
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=False)
    admission_year = Column(Integer, nullable=False)
    enrollments = relationship("Enrollment", back_populates="student")


    def __repr__(self):
        return f"<Student {self.name}>"

class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    subjects = relationship("Subject", back_populates="instructor")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    credit_hours = Column(Integer, nullable=False)

    instructor_id = Column(Integer, ForeignKey("instructors.id"))

    instructor = relationship("Instructor", back_populates="subjects")
    enrollments = relationship("Enrollment", back_populates="subject")


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    semester = Column(Integer)

    # Examination System
    mid_marks = Column(Float, default=0)
    final_marks = Column(Float, default=0)
    internal_marks = Column(Float, default=0)

    total_marks = Column(Float, default=0)
    grade = Column(String)
    grade_points = Column(Float)

    status = Column(String, default="active")  # active, completed, dropped

    student = relationship("Student", back_populates="enrollments")
    subject = relationship("Subject", back_populates="enrollments")

    def __repr__(self):
        return f"<Enrollment student_id={self.student_id} subject_id={self.subject_id}>"



