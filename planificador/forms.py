from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class FormularioRegistroUsuario(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Confirmación de contraseña",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for nombre, campo in self.fields.items():
            widget = campo.widget
            widget.attrs["class"] = "form-control"

        self.fields["username"].widget.attrs["placeholder"] = "Elige un nombre de usuario"
        self.fields["email"].widget.attrs["placeholder"] = "correo@ejemplo.com"
        self.fields["password1"].widget.attrs["placeholder"] = "Crea una contraseña"
        self.fields["password2"].widget.attrs["placeholder"] = "Repite la contraseña"

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data["email"]

        if commit:
            usuario.save()

        return usuario