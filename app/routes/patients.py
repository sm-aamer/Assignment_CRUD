from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.patients import PatientCreate, PatientResponse
from app.crud.patients import *

router = APIRouter(prefix='/patient', tags=['Patients'])


@router.post('/', response_model=PatientResponse)
def create_patient_route(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)


@router.get('/')
def get_all_patient(db: Session = Depends(get_db)):
    return get_patient(db)

@router.get('/{patient_id}', response_model=PatientResponse)
def get_patients_route(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patients(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.put('/{patient_id}')
def update_patient_route(
    patient_id: int, 
    patient: PatientCreate, 
    db: Session = Depends(get_db)
    ):
    updated_patient = update_patient(db, patient_id, patient)
    if not updated_patient:
        raise HTTPException(
            status_code=404, 
            detail="Patient not found")
    return updated_patient

@router.delete('/{patient_id}')
def delete_patient_route(patient_id: int, db: Session = Depends(get_db)):
    deleted_patient = delete_patient(db, patient_id)
    if not deleted_patient:
        raise HTTPException(
            status_code=404, 
            detail="Patient not found")
    return {"message": "Patient deleted successfully"}
