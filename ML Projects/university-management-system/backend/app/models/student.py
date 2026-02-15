from sqlalchemy import Column, Integer, String
from app.database.db import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=False)
    admission_year = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Student {self.name}>"
