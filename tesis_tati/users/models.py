from django.db import models
from common.models import BaseModel

# Create your models here.

class Usuario(BaseModel):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre + " " + self.apellido + " - (" + self.email + ")"

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"