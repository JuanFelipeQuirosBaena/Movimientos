from django.db import models
from django.contrib.auth.models import User

class TipoMovimiento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
