from django.db import models
from common.models import BaseModel

# Create your models here.

class Usuario(BaseModel):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre + " (" + str(self.pk) + ") "

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"