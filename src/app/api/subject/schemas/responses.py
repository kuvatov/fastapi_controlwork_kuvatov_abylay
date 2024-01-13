from datetime import datetime
from uuid import UUID
from core.schemas import BaseModel


class SubjectGet(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    name: str
    description: str
    