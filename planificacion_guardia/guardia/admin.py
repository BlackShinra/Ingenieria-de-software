from django.contrib import admin

from .models import Guardia, Horario, Plantilla

# Register your models here.

admin.site.register(Guardia)
admin.site.register(Plantilla)
admin.site.register(Horario)
