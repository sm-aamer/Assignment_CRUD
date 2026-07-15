from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.patients import create_patient, delete_patient, get_patient, get_patients, update_patient
from app.database import get_db
from app.schemas.patients import PatientCreate, PatientResponse, PatientUpdate

router = APIRouter(prefix="/patients", tags=["patients"])


@router.post("/", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient_route(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db=db, patient=patient)


@router.get("/", response_model=list[PatientResponse])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_patients(db=db, skip=skip, limit=limit)


@router.get("/{patient_id}", response_model=PatientResponse)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = get_patient(db=db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient_route(patient_id: int, patient: PatientUpdate, db: Session = Depends(get_db)):
    updated_patient = update_patient(db=db, patient_id=patient_id, patient=patient)
    if updated_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated_patient


@router.delete("/{patient_id}")
def delete_patient_route(patient_id: int, db: Session = Depends(get_db)):
    deleted_patient = delete_patient(db=db, patient_id=patient_id)
    if deleted_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted successfully"}
