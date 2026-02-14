import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(title=os.getenv("PROJECT_NAME"))

@app.get("/")
def root():
    return {"message": "Running Successfully"}
