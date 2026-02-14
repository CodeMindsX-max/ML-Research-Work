import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.database.db import engine

load_dotenv()

app = FastAPI(title=os.getenv("PROJECT_NAME"))

@app.get("/")
def root():
    return {"message": "Database Connected Successfully"}
