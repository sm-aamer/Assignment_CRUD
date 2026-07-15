from sqlalchemy.orm import Session

from app.model.patients import Patients
from app.schemas.patients import PatientCreate, PatientUpdate


def get_patient(db: Session, patient_id: int):
    return db.query(Patients).filter(Patients.id == patient_id).first()


def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Patients).offset(skip).limit(limit).all()


def create_patient(db: Session, patient: PatientCreate):
    db_patient = Patients(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def update_patient(db: Session, patient_id: int, patient: PatientUpdate):
    db_patient = get_patient(db, patient_id)
    if not db_patient:
        return None

    for key, value in patient.model_dump(exclude_unset=True).items():
        setattr(db_patient, key, value)

    db.commit()
    db.refresh(db_patient)
    return db_patient


def delete_patient(db: Session, patient_id: int):
    db_patient = get_patient(db, patient_id)
    if not db_patient:
        return None

    db.delete(db_patient)
    db.commit()
    return db_patient
