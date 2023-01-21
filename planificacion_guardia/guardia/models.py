from django.db import models
from django.contrib.auth.models import User


class Horario(models.Model):
    nombre = models.CharField(max_length=255)
    sesion = models.CharField(max_length=255)
    paridad = models.CharField(max_length=255)
    dia = models.DateField(max_length=255)

    def __str__(self):
        return self.nombre



class Guardia(models.Model):
    lugar = models.CharField(max_length=255)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.lugar


class Plantilla(models.Model):
    asignatura = models.CharField(max_length=255)
    turno = models.CharField(max_length=255)
    semana = models.IntegerField()
    local = models.CharField(max_length=255)
    guardia = models.ForeignKey(Guardia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.asignatura}, {self.local}'
