import time

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView

from .forms import NewUserForm, UsuarioForm, SelectGroupForm
from .models import Usuario


# Create your views here.


class AdminUserMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return render(template_name='error_permisos.html', request=self.request)


class UsuarioListView(AdminUserMixin,ListView):
    model = Usuario
    context_object_name = 'usuario_list'


class Usuario_Delete(AdminUserMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('gest_usuarios')


#TODO Anadir la asignacion de grupos
class CrearUsuarioView(AdminUserMixin,View):

    def get(self, request):
        user_form = NewUserForm()
        usuario_form = UsuarioForm()
        group_form = SelectGroupForm()
        return render(request, 'usuarios/crear_usuario.html', {
            'user_form': user_form,
            'usuario_form': usuario_form,
            'group_form': group_form
        })

    def post(self, request):
        user_form = NewUserForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        group_form = SelectGroupForm(request.POST)
        if user_form.is_valid() and usuario_form.is_valid() and group_form.is_valid():
            db_user = user_form.save()
            newuser = usuario_form.save(commit=False)
            newuser.db_user = User.objects.get(pk=db_user.id)
            group = Group.objects.get(pk=group_form.cleaned_data['grupo'].id)
            group.user_set.add(db_user)
            newuser.save()
            return redirect('gest_usuarios')
        return render(request, 'usuarios/crear_usuario.html', {
            'user_form': user_form,
            'usuario_form': usuario_form,
            'group_form': group_form
        })


#Todo Implementar Modificar Usuario
class ModificarUsuarioView(LoginRequiredMixin,View):

    def get(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        user_form = NewUserForm(instance=usuario.db_user)
        usuario_form = UsuarioForm(instance=usuario)
        group_form = SelectGroupForm()
        return render(request, 'usuarios/crear_usuario.html', {
            'user_form': user_form,
            'usuario_form': usuario_form,
            'group_form': group_form
        })

    def post(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        user_form = NewUserForm(request.POST,instance=usuario.db_user)
        usuario_form = UsuarioForm(request.POST,instance=usuario)
        group_form = SelectGroupForm(request.POST)
        if user_form.is_valid() and usuario_form.is_valid() and group_form.is_valid():
            user_form.save()
            usuario_form.save(commit=False)
            group = Group.objects.get(pk=group_form.cleaned_data['grupo'].id)
            group.user_set.add(usuario.db_user)
            return redirect('gest_usuarios')
        return render(request, 'usuarios/crear_usuario.html', {
            'user_form': user_form,
            'usuario_form': usuario_form,
            'group_form': group_form
        })