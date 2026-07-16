from fastapi import FastAPI
from app.routes.patients import router as patient_router

app = FastAPI()

app.include_router(patient_router)

@app.get('/')
def home():
    return {"message": "Welcome to the Patient Management System!"}

