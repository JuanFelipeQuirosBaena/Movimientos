from django import forms
from django.core.validators import RegexValidator
from .models import Movimiento, TipoMovimiento


class TipoMovimientoForm(forms.ModelForm):
    """Formulario para crear y editar tipos de movimiento."""

    nombre = forms.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message='El nombre solo debe contener letras y espacios.',
            )
        ],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del tipo'}),
        error_messages={
            'required': 'El nombre del tipo de movimiento es obligatorio.',
            'max_length': 'El nombre no puede exceder 50 caracteres.',
        },
    )

    descripcion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción opcional'}),
    )

    class Meta:
        model = TipoMovimiento
        fields = ['nombre', 'descripcion']


class MovimientoForm(forms.ModelForm):
    """Formulario para crear y editar movimientos."""

    class Meta:
        model = Movimiento
        fields = ['tipo_movimiento']

    def __init__(self, *args, **kwargs):
        super(MovimientoForm, self).__init__(*args, **kwargs)
        # Aplicar clases de Bootstrap 5
        self.fields['tipo_movimiento'].widget.attrs.update({'class': 'form-select'})
        self.fields['tipo_movimiento'].empty_label = '--- Seleccione un tipo ---'
        self.fields['tipo_movimiento'].error_messages = {
            'required': 'Por favor, selecciona un tipo de movimiento.',
            'invalid_choice': 'El tipo de movimiento seleccionado no es válido.',
        }

    def clean_tipo_movimiento(self):
        """Validación del servidor para el campo tipo_movimiento."""
        tipo = self.cleaned_data.get('tipo_movimiento')
        if tipo is None:
            raise forms.ValidationError('Debes seleccionar un tipo de movimiento válido.')
        return tipo
