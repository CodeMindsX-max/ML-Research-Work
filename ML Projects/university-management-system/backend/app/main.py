import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.database.db import engine, Base
from app.models import student

load_dotenv()

app = FastAPI(title=os.getenv("PROJECT_NAME"))

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Student Table Ready"}
