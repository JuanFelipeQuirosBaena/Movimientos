from django.contrib import admin
from .models import TipoMovimiento, Movimiento


@admin.register(TipoMovimiento)
class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('id_movimiento', 'tipo_movimiento', 'usuario', 'created_at', 'updated_at')
    list_filter = ('tipo_movimiento', 'usuario')
    search_fields = ('tipo_movimiento__nombre', 'usuario__username')
    readonly_fields = ('created_at', 'updated_at')
