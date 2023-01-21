from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'solapin', 'departamento']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'solapin': forms.TextInput(attrs={'placeholder': 'Solapin'}),
            'departamento': forms.TextInput(
                attrs={'placeholder': 'Departamento'}),
        }


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat password'})


class SelectGroupForm(forms.Form):
    grupo = forms.ModelChoiceField(queryset=Group.objects.all())