from tortoise import fields
from .base import BaseModel


class Subject(BaseModel):
    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta(BaseModel.Meta):
        table = 'subject'
        