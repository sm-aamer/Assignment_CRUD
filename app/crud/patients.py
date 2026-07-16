from typing import Any

from sqlalchemy.orm import Session
from app.model.patients import Patients
from app.schemas.patients import PatientCreate, PatientResponse


def create_patient(db: Session, patient: PatientCreate):
    db_patient = Patients(
        name=patient.name, 
        age=patient.age, 
        description=patient.description
        )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db: Session):
    return db.query(Patients).all()


def get_patients(db: Session, patient_id: int):
    return db.query(Patients).filter(
        Patients.id == patient_id
        ).first()

def update_patient(
        db: Session, 
        patient_id: int, 
        patient: PatientCreate):
    patient_db = get_patients(db, patient_id)
    if not patient_db:
        return None
    patient_db.name = patient.name
    patient_db.age = patient.age
    patient_db.description = patient.description
    
    db.commit()
    db.refresh(patient_db)
    
    return patient_db

def delete_patient(db: Session, patient_id: int):
    patient_db = get_patients(db, patient_id)
    if not patient_db:
        return None
    db.delete(patient_db)
    db.commit()
    return patient_db
