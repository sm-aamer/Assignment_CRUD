from fastapi import FastAPI

from app.database import Base, engine, validate_database_connection
from app.model.patients import Patients
from app.routes.patients import router as patient_router

app = FastAPI(title="Patient Management System")

validate_database_connection()
Base.metadata.create_all(bind=engine)

app.include_router(patient_router)
