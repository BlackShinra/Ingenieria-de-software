"""planificacion_guardia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

#TODO adicionar modificar
urlpatterns = [
    #Listar
    path("", GuardiaListView.as_view(), name="gest_guardias"),
    path("gestionar_horarios/", HorarioListView.as_view(), name="gest_horarios"),
    path("gestionar_plantillas/", PlantillaListView.as_view(), name="gest_plantillas"),
    #Crear
    path("crear_plantilla/", PlantillaCreateView.as_view(), name="crear_plantilla"),
    path("crear_horario/", HorarioCreateView.as_view(), name="crear_horario"),
    path("crear_guardia/", GuardiaCreateView.as_view(), name="crear_guardia"),
    #Eliminar
    path("delete_guardia/<int:pk>", DeleteGuardiaView.as_view(), name="delete_guardia"),
    path("delete_horario/<int:pk>", DeleteHorarioView.as_view(), name="delete_horario"),
    path("delete_plantilla/<int:pk>", DeletePlantillaView.as_view(), name="delete_plantilla"),
    #Modificar
    path("edit_plantilla/<int:pk>", UpdatePlantillaView.as_view(), name="edit_plantilla"),
    path("edit_horario/<int:pk>", UpdateHorarioView.as_view(), name="edit_horario"),
    path("edit_guardia/<int:pk>", UpdateGuardiaView.as_view(), name="edit_guardia")
]
