from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
from common.models import BaseModel
from users.models import Usuario

# Create your models here.
class Comment(BaseModel):
    user  = ForeignKey(Usuario, on_delete=models.CASCADE, related_name="comentarios")
    text = TextField(max_length=2000)
    