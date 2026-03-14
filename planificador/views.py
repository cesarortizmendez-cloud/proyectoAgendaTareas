from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FormularioTarea
from .models import Materia, Tarea


def inicio(request):
    total_materias = Materia.objects.count()
    total_tareas = Tarea.objects.count()
    tareas_pendientes = Tarea.objects.filter(completada=False).count()

    contexto = {
        "titulo_pagina": "Inicio",
        "total_materias": total_materias,
        "total_tareas": total_tareas,
        "tareas_pendientes": tareas_pendientes,
    }
    return render(request, "planificador/inicio.html", contexto)


def lista_tareas(request):
    tareas = Tarea.objects.select_related("materia").all()

    contexto = {
        "titulo_pagina": "Lista de tareas",
        "tareas": tareas,
    }
    return render(request, "planificador/lista_tareas.html", contexto)


def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea.objects.select_related("materia"), id=tarea_id)

    contexto = {
        "titulo_pagina": f"Detalle de {tarea.titulo}",
        "tarea": tarea,
    }
    return render(request, "planificador/detalle_tarea.html", contexto)


def crear_tarea(request):
    if request.method == "POST":
        formulario = FormularioTarea(request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La tarea fue creada correctamente.")
            return redirect("lista_tareas")
    else:
        formulario = FormularioTarea()

    contexto = {
        "titulo_pagina": "Nueva tarea",
        "titulo_formulario": "Crear tarea",
        "boton_envio": "Guardar tarea",
        "formulario": formulario,
    }
    return render(request, "planificador/formulario_tarea.html", contexto)


def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == "POST":
        formulario = FormularioTarea(request.POST, instance=tarea)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La tarea fue actualizada correctamente.")
            return redirect("detalle_tarea", tarea_id=tarea.id)
    else:
        formulario = FormularioTarea(instance=tarea)

    contexto = {
        "titulo_pagina": f"Editar {tarea.titulo}",
        "titulo_formulario": "Editar tarea",
        "boton_envio": "Guardar cambios",
        "formulario": formulario,
        "tarea": tarea,
    }
    return render(request, "planificador/formulario_tarea.html", contexto)


def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == "POST":
        titulo_tarea = tarea.titulo
        tarea.delete()
        messages.success(request, f'La tarea "{titulo_tarea}" fue eliminada correctamente.')
        return redirect("lista_tareas")

    contexto = {
        "titulo_pagina": f"Eliminar {tarea.titulo}",
        "tarea": tarea,
    }
    return render(request, "planificador/confirmar_eliminar_tarea.html", contexto)