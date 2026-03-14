from django.shortcuts import get_object_or_404, render
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