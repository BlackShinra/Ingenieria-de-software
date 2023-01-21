from django.db import models
from django.contrib.auth.models import User

# Create your models here. Admin Planificador


class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    solapin = models.CharField(max_length=15)
    apellido = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    db_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
