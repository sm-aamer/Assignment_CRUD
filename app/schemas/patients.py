from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class PatientBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    date_of_admission: date
    ward: str


class PatientCreate(PatientBase):
    pass


class PatientUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_admission: Optional[date] = None
    ward: Optional[str] = None


class PatientResponse(PatientBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
