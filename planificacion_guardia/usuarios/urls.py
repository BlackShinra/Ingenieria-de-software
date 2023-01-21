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
from .views import UsuarioListView, Usuario_Delete, CrearUsuarioView, ModificarUsuarioView

urlpatterns = [
    path('gestionar_usuarios/', UsuarioListView.as_view(), name='gest_usuarios'),
    path('delete_user/<int:pk>', Usuario_Delete.as_view(), name = 'user_delete'),
    path('crear_usuario', CrearUsuarioView.as_view(), name='crear_user'),
    path('edit_usuario/<int:pk>', ModificarUsuarioView.as_view(), name='edit_usuario')
]
