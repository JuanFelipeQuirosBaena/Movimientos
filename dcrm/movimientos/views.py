from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movimiento
from .forms import MovimientoForm

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser
        
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos de administrador para realizar esta acción.")
        return redirect('movimientos:list')

class MovimientoListView(LoginRequiredMixin, ListView):
    model = Movimiento
    template_name = 'movimientos/movimiento_list.html'
    context_object_name = 'movimientos'
    ordering = ['-created_at']
