
# Register your models here.
from django.contrib import admin
from .models import Materia, Tarea


@admin.register(Materia) #decorador para registrar el modelo Materia en la interfaz de administración de Django
class MateriaAdmin(admin.ModelAdmin):  #clase para personalizar la administración del modelo Materia
    list_display = ("nombre", "creada_en") #campos que se mostrarán en la lista de materias en la interfaz de administración
    search_fields = ("nombre",) #campos que se podrán buscar en la interfaz de administración para facilitar la búsqueda de materias

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "usuario", "materia", "fecha_entrega", "prioridad", "completada")
    list_filter = ("usuario", "prioridad", "completada", "materia")
    search_fields = ("titulo", "descripcion")
    list_editable = ("completada",)