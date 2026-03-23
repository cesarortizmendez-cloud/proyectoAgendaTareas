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
            "descripcion": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()

        if len(titulo) < 3:
            raise forms.ValidationError("El título debe tener al menos 3 caracteres.")

        return titulo