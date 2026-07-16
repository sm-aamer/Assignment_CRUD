from pydantic import BaseModel



class PatientCreate(BaseModel):
    name: str
    age: int
    description: str|None = None



class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    description: str|None = None

    class config:
        from_attributes = True


