from tortoise import fields
from .base import BaseModel


class Material(BaseModel):
    topic = fields.CharField(max_length=255)
    content = fields.TextField(null=True)
    subject = fields.ForeignKeyField(
        model_name='models.Subject',
        related_name='materials',
        null=True,
    )
    
    def __str__(self) -> str:
        return self.topic
    
    class Meta(BaseModel.Meta):
        table = 'material'
        