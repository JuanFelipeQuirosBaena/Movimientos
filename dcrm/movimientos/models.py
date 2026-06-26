from django.db import models
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
