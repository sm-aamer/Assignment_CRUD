from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Patients(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
