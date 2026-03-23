from django import forms
from .models import Tarea


class FormularioTarea(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            "materia",
            "titulo",
            "descripcion",
            "fecha_entrega",
            "prioridad",
            "completada",
        ]
        labels = {
            "materia": "Materia",
            "titulo": "Título",
            "descripcion": "Descripción",
            "fecha_entrega": "Fecha de entrega",
            "prioridad": "Prioridad",
            "completada": "Completada",
        }
        widgets = {
            "fecha_entrega": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for nombre, campo in self.fields.items():
            widget = campo.widget

            if isinstance(widget, forms.CheckboxInput):
                widget.attrs["class"] = "form-check-input"
            elif isinstance(widget, forms.Select):
                widget.attrs["class"] = "form-select"
            elif isinstance(widget, forms.Textarea):
                widget.attrs["class"] = "form-control"
                widget.attrs["rows"] = 4
            else:
                widget.attrs["class"] = "form-control"

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()

        if len(titulo) < 3:
            raise forms.ValidationError(
                "El título debe tener al menos 3 caracteres."
            )

        return titulo