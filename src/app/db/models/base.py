from uuid import uuid4
from tortoise import models, fields


class IdMixin(models.Model):
    id = fields.UUIDField(pk=True, default=uuid4)
    
    class Meta:
        abstract = True
        
        
class TimestampMixin(models.Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
        
class BaseModel(IdMixin, TimestampMixin):
    
    class Meta:
        ordering = ['-created_at', ]
        