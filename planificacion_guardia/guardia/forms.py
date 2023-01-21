from django import forms
from django.contrib.auth.models import Group

from .models import Horario, Plantilla, Guardia


class GuardiaForm(forms.ModelForm):
    class Meta:
        model = Guardia
        fields = ['lugar', 'horario', 'usuario']
        widgets = {
            'lugar': forms.TextInput(attrs={'placeholder': 'Lugar'}),
        }



class PlantillaForm(forms.ModelForm):
    class Meta:
        model = Plantilla
        fields = ['asignatura', 'turno', 'semana', 'local', 'guardia', ]
        widgets = {
            'asignatura': forms.TextInput(attrs={'placeholder': 'Asignatura'}),
            'turno': forms.TextInput(attrs={'placeholder': 'Turno'}),
            'semana': forms.TextInput(attrs={'placeholder': 'Semana'}),
            'local': forms.TextInput(
                attrs={'placeholder': 'Local'}),
        }


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['nombre', 'sesion', 'paridad', 'dia']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'sesion': forms.TextInput(attrs={'placeholder': 'Sesion'}),
            'paridad': forms.TextInput(attrs={'placeholder': 'Paridad'}),
            'dia': forms.SelectDateWidget(
                attrs={'placeholder': 'Dia'}),
        }





