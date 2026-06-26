from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movimiento
from .forms import MovimientoForm


class AdminRequiredMixin(UserPassesTestMixin):
    """Mixin que restringe el acceso a usuarios con permisos de administrador."""

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos de administrador para realizar esta acción.")
        return redirect('movimientos:list')


class MovimientoListView(LoginRequiredMixin, ListView):
    """Vista para listar todos los movimientos registrados."""
    login_url = 'home'
    model = Movimiento
    template_name = 'movimientos/movimiento_list.html'
    context_object_name = 'movimientos'
    ordering = ['-created_at']


class MovimientoDetailView(LoginRequiredMixin, DetailView):
    """Vista para ver el detalle de un movimiento específico."""
    login_url = 'home'
    model = Movimiento
    template_name = 'movimientos/movimiento_detail.html'
    context_object_name = 'movimiento'


class MovimientoCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    """Vista para crear un nuevo movimiento. Solo accesible por administradores."""
    login_url = 'home'
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'movimientos/movimiento_create.html'
    success_url = reverse_lazy('movimientos:list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Movimiento creado exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al crear el movimiento. Revisa los datos ingresados.")
        return super().form_invalid(form)


class MovimientoUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    """Vista para editar un movimiento existente. Solo accesible por administradores."""
    login_url = 'home'
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'movimientos/movimiento_update.html'
    success_url = reverse_lazy('movimientos:list')

    def form_valid(self, form):
        messages.success(self.request, "Movimiento actualizado exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al actualizar el movimiento. Revisa los datos ingresados.")
        return super().form_invalid(form)


class MovimientoDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    """Vista para eliminar un movimiento. Solo accesible por administradores."""
    login_url = 'home'
    model = Movimiento
    template_name = 'movimientos/movimiento_delete.html'
    success_url = reverse_lazy('movimientos:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Movimiento eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)

