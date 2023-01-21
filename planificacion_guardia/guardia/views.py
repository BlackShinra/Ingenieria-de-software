from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import HorarioForm, PlantillaForm, GuardiaForm
from .models import Guardia, Plantilla, Horario


# Create your views here.

class PlanificadorUserMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        if self.request.user.is_staff:
            return False
        else:
            return self.request.user.groups.first().name == "Planificador"

    def handle_no_permission(self):
        return render(request = self.request ,template_name='error_permisos.html')


class ProfesorUserMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        if self.request.user.is_staff:
            return False
        else:
            return self.request.user.groups.first().name == "ProfesorGD"

    def handle_no_permission(self):
        return render(request = self.request ,template_name='error_permisos.html')


class GuardiaListView(ListView):
    model = Guardia
    context_object_name = 'guardia_list'


class PlantillaListView(ListView):
    model = Plantilla
    context_object_name = 'plantilla_list'


class HorarioListView(ListView):
    model = Horario
    context_object_name = 'horario_list'


class HorarioCreateView(PlanificadorUserMixin,CreateView):
    model = Horario
    template_name = 'nuevo_horario.html'
    form_class = HorarioForm
    success_url = reverse_lazy('gest_horarios')


class PlantillaCreateView(ProfesorUserMixin, CreateView):
    model = Plantilla
    template_name = 'nueva_plantilla.html'
    form_class = PlantillaForm
    success_url = reverse_lazy('gest_plantillas')


class GuardiaCreateView(PlanificadorUserMixin,CreateView):
    model = Guardia
    template_name = 'nueva_guardia.html'
    form_class = GuardiaForm
    success_url = reverse_lazy('gest_guardias')

    def form_valid(self, form):
        self.object = form.save()

        self.object.usuario = self.request.user

        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class DeleteGuardiaView(PlanificadorUserMixin, DeleteView):
    model = Guardia
    success_url = reverse_lazy('gest_guardias')


class DeleteHorarioView(PlanificadorUserMixin, DeleteView):
    model = Horario
    success_url = reverse_lazy('gest_horarios')


class DeletePlantillaView(ProfesorUserMixin, DeleteView):
    model = Plantilla
    success_url = reverse_lazy('gest_plantillas')


class UpdateHorarioView(PlanificadorUserMixin, UpdateView):
    model = Horario
    success_url = reverse_lazy('gest_horarios')
    form_class = HorarioForm
    template_name = 'horario_edit.html'


class UpdatePlantillaView(ProfesorUserMixin, UpdateView):
    model = Plantilla
    form_class = PlantillaForm
    template_name = 'plantilla_edit.html'
    success_url = reverse_lazy('gest_plantillas')


class UpdateGuardiaView(PlanificadorUserMixin, UpdateView):
    model = Guardia
    form_class = GuardiaForm
    template_name = 'guardia_edit.html'
    success_url = reverse_lazy('gest_guardias')
