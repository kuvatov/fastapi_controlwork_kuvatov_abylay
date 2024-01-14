from pydantic import Field
from datetime import datetime
from uuid import UUID
from core.schemas import BaseModel
from api.material.schemas.requests import MaterialGet


class SubjectBase(BaseModel):
    name: str
    description: str
    
    
class SubjectAllOptional(BaseModel):
    name: str | None = Field(None)
    description: str | None = Field(None)
    id: UUID | None = Field(None)
    created_at: datetime | None = Field(None)
    updated_at: datetime | None = Field(None)
    
    
class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(SubjectAllOptional):
    pass


class SubjectGet(SubjectAllOptional):
    # materials: list[MaterialGet]
    pass
