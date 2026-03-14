
# Create your views here.

from django.shortcuts import render


def inicio(request):
    contexto = {
        "titulo": "Agenda de estudio",
        "mensaje": "Tu proyecto Django ya está funcionando.",
    }
    return render(request, "planificador/inicio.html", contexto)