from pydantic import Field
from datetime import datetime
from uuid import UUID
from core.schemas import BaseModel


class MaterialBase(BaseModel):
    topic: str
    content: str
    
    
class MaterialAllOptional(BaseModel):
    topic: str | None = Field(None)
    content: str | None = Field(None)
    id: UUID | None = Field(None)
    created_at: datetime | None = Field(None)
    updated_at: datetime | None = Field(None)
    
    
class MaterialCreate(MaterialBase):
    subject_id: UUID


class MaterialUpdate(MaterialAllOptional):
    pass


class MaterialGet(MaterialAllOptional):
    pass
