from django import forms
from .models import Movimiento

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ['tipo_movimiento'] # 'usuario' is set automatically in the view
        
    def __init__(self, *args, **kwargs):
        super(MovimientoForm, self).__init__(*args, **kwargs)
        # Aplicar clases de Bootstrap 5
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
        
        self.fields['tipo_movimiento'].error_messages = {
            'required': 'Por favor, selecciona un tipo de movimiento.',
            'invalid': 'El tipo de movimiento seleccionado no es válido.'
        }
