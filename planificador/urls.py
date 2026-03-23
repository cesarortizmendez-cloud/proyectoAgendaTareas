
from django.urls import path
#se importan las vistas que se utilizarán para manejar las diferentes rutas de la aplicación
from .views import (
    CrearTareaView,
    DetalleTareaView,
    EditarTareaView,
    EliminarTareaView,
    InicioView,
    ListaTareasView,
    RegistroUsuarioView,
)

urlpatterns = [
    path("", InicioView.as_view(), name="inicio"),
     path("registro/", RegistroUsuarioView.as_view(), name="registro"),
    path("tareas/", ListaTareasView.as_view(), name="lista_tareas"),
    path("tareas/nueva/", CrearTareaView.as_view(), name="crear_tarea"),
    path("tareas/<int:tarea_id>/", DetalleTareaView.as_view(), name="detalle_tarea"),
    path("tareas/<int:tarea_id>/editar/", EditarTareaView.as_view(), name="editar_tarea"),
    path("tareas/<int:tarea_id>/eliminar/", EliminarTareaView.as_view(), name="eliminar_tarea"),
]