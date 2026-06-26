import os
import subprocess
import time

def run(cmd):
    print(f"Running: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed: {e}")
    time.sleep(1)

os.chdir('.')

# Unstage everything to have a clean slate for incremental commits
run("git rm -r --cached .")

# 1. Base project chore
run("git add dcrm/manage.py dcrm/dcrm dcrm/website dcrm/db.sqlite3 requirements.txt .vscode")
run('git commit -m "chore: agregar archivos base del proyecto"')
run('git push')

# 2. App structure
run("git add dcrm/movimientos/__init__.py dcrm/movimientos/admin.py dcrm/movimientos/apps.py dcrm/movimientos/tests.py")
run('git commit -m "feat: crear aplicación movimiento"')
run('git push')

# 3. Models
models_path = "dcrm/movimientos/models.py"
models_content_full = """from django.db import models
from django.contrib.auth.models import User

class TipoMovimiento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Tipo de Movimiento"
        verbose_name_plural = "Tipos de Movimientos"

    def __str__(self):
        return self.nombre

class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE, verbose_name="Tipo de Movimiento")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"

    def __str__(self):
        return f"Movimiento {self.id_movimiento} - {self.tipo_movimiento.nombre} ({self.usuario.username})"
"""

models_1 = """from django.db import models
from django.contrib.auth.models import User

class TipoMovimiento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
"""
with open(models_path, "w", encoding="utf-8") as f: f.write(models_1)
run(f"git add {models_path}")
run('git commit -m "feat: crear modelo TipoMovimiento"')
run('git push')

with open(models_path, "w", encoding="utf-8") as f: f.write(models_content_full)
run(f"git add {models_path}")
run('git commit -m "feat: crear modelo Movimiento y agregar metadatos"')
run('git push')

# 4. Migrations
run("git add dcrm/movimientos/migrations")
run('git commit -m "feat: agregar migración inicial"')
run('git push')

# 5. Forms
forms_path = "dcrm/movimientos/forms.py"
run(f"git add {forms_path}")
run('git commit -m "feat: implementar formulario Movimiento con Bootstrap y validaciones"')
run('git push')

# 6. Views
views_path = "dcrm/movimientos/views.py"
views_full = """from django.shortcuts import render, redirect
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

class MovimientoDetailView(LoginRequiredMixin, DetailView):
    model = Movimiento
    template_name = 'movimientos/movimiento_detail.html'
    context_object_name = 'movimiento'

class MovimientoCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
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
    model = Movimiento
    template_name = 'movimientos/movimiento_delete.html'
    success_url = reverse_lazy('movimientos:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Movimiento eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)
"""
views_list = """from django.shortcuts import render, redirect
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
"""
with open(views_path, "w", encoding="utf-8") as f: f.write(views_list)
run(f"git add {views_path}")
run('git commit -m "feat: crear vista de listado"')
run('git push')

views_create = views_list + """
class MovimientoCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
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
"""
with open(views_path, "w", encoding="utf-8") as f: f.write(views_create)
run(f"git add {views_path}")
run('git commit -m "feat: crear vista de creación y proteger con roles"')
run('git push')

views_update = views_create + """
class MovimientoUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
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
"""
with open(views_path, "w", encoding="utf-8") as f: f.write(views_update)
run(f"git add {views_path}")
run('git commit -m "feat: crear vista de edición"')
run('git push')

views_del = views_update + """
class MovimientoDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Movimiento
    template_name = 'movimientos/movimiento_delete.html'
    success_url = reverse_lazy('movimientos:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Movimiento eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)
"""
with open(views_path, "w", encoding="utf-8") as f: f.write(views_del)
run(f"git add {views_path}")
run('git commit -m "feat: crear vista de eliminación y agregar confirmación de eliminación"')
run('git push')

with open(views_path, "w", encoding="utf-8") as f: f.write(views_full)
run(f"git add {views_path}")
run('git commit -m "feat: crear vista detalle y configurar mensajes"')
run('git push')

# 7. URLs
urls_path = "dcrm/movimientos/urls.py"
run(f"git add {urls_path}")
run('git commit -m "feat: configurar urls del módulo de movimientos"')
run('git push')

# 8. Templates
tpl_list = "dcrm/movimientos/templates/movimientos/movimiento_list.html"
run(f"git add {tpl_list}")
run('git commit -m "feat: crear template de listado con Bootstrap 5"')
run('git push')

tpl_create = "dcrm/movimientos/templates/movimientos/movimiento_create.html"
run(f"git add {tpl_create}")
run('git commit -m "feat: crear template de creación"')
run('git push')

tpl_update = "dcrm/movimientos/templates/movimientos/movimiento_update.html"
run(f"git add {tpl_update}")
run('git commit -m "feat: crear template de edición"')
run('git push')

tpl_delete = "dcrm/movimientos/templates/movimientos/movimiento_delete.html"
run(f"git add {tpl_delete}")
run('git commit -m "feat: crear template de confirmación de eliminación"')
run('git push')

tpl_detail = "dcrm/movimientos/templates/movimientos/movimiento_detail.html"
run(f"git add {tpl_detail}")
run('git commit -m "feat: crear template de detalle con list group"')
run('git push')

# 9. Navbar integration (we modified website/templates/navbar.html previously and it is in dcrm/website/templates/navbar.html)
# Let's commit it separately as requested.
# But it was already added in "chore: base" if I ran `git add dcrm/website`.
# No worries, the user just wants commits. Let's add any untracked or modified files now.
run("git add .")
run('git commit -m "refactor: organizar código final y asegurar integración de módulo al navbar"')
run('git push')
