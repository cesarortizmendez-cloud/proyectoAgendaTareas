from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .forms import FormularioTarea
from .models import Materia, Tarea


class InicioView(TemplateView):
    template_name = "planificador/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            tareas_usuario = Tarea.objects.filter(usuario=self.request.user)
        else:
            tareas_usuario = Tarea.objects.none()

        context.update({
            "titulo_pagina": "Inicio",
            "total_materias": Materia.objects.count(),
            "total_tareas": tareas_usuario.count(),
            "tareas_pendientes": tareas_usuario.filter(completada=False).count(),
        })
        return context


class ListaTareasView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = "planificador/lista_tareas.html"
    context_object_name = "tareas"
    paginate_by = 5

    def get_queryset(self):
        return (
            Tarea.objects.select_related("materia")
            .filter(usuario=self.request.user)
            .order_by("completada", "fecha_entrega", "titulo")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Mis tareas"
        return context


class DetalleTareaView(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = "planificador/detalle_tarea.html"
    context_object_name = "tarea"
    pk_url_kwarg = "tarea_id"

    def get_queryset(self):
        return Tarea.objects.select_related("materia").filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = f"Detalle de {self.object.titulo}"
        return context


class CrearTareaView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = FormularioTarea
    template_name = "planificador/formulario_tarea.html"
    success_url = reverse_lazy("lista_tareas")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "La tarea fue creada correctamente.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "titulo_pagina": "Nueva tarea",
            "titulo_formulario": "Crear tarea",
            "boton_envio": "Guardar tarea",
        })
        return context


class EditarTareaView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = FormularioTarea
    template_name = "planificador/formulario_tarea.html"
    context_object_name = "tarea"
    pk_url_kwarg = "tarea_id"

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "La tarea fue actualizada correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("detalle_tarea", kwargs={"tarea_id": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "titulo_pagina": f"Editar {self.object.titulo}",
            "titulo_formulario": "Editar tarea",
            "boton_envio": "Guardar cambios",
        })
        return context


class EliminarTareaView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "planificador/confirmar_eliminar_tarea.html"
    context_object_name = "tarea"
    pk_url_kwarg = "tarea_id"
    success_url = reverse_lazy("lista_tareas")

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, f'La tarea "{self.object.titulo}" fue eliminada correctamente.')
        return super().form_valid(form)