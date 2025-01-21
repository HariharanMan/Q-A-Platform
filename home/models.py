from django.db import models
import uuid
import random

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable = True)
    created_at = models.DateFeild(auto_now_add =True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True
    
class Types(BaseModel):
    gfg_name = models.CharField(max_length=100)
    def __str__(self):
        return self.gfg_name