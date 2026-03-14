from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("tareas/", views.lista_tareas, name="lista_tareas"),
    path("tareas/nueva/", views.crear_tarea, name="crear_tarea"),
    path("tareas/<int:tarea_id>/", views.detalle_tarea, name="detalle_tarea"),
    path("tareas/<int:tarea_id>/editar/", views.editar_tarea, name="editar_tarea"),
    path("tareas/<int:tarea_id>/eliminar/", views.eliminar_tarea, name="eliminar_tarea"),
]