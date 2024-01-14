from datetime import datetime
from uuid import UUID
from core.schemas import BaseModel


class MaterialGet(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    topic: str
    content: str
    subject_id: UUID
    