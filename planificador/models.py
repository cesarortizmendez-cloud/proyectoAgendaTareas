
# Create your models here.
from django.conf import settings
from django.db import models


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]  #las materias se ordenan por nombre
        verbose_name = "materia"  #nombre en singular para la interfaz de administración
        verbose_name_plural = "materias" #nombre en plural para la interfaz de administración

    def __str__(self):
        return self.nombre #representación legible de la materia, se muestra en la interfaz de administración y en otros lugares donde se necesite mostrar el nombre de la materia


class Tarea(models.Model):
    PRIORIDAD_OPCIONES = [
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tareas",
        null=True,
        blank=True,
    )
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name="tareas",
    )
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    fecha_entrega = models.DateField()
    prioridad = models.CharField(
        max_length=10,
        choices=PRIORIDAD_OPCIONES,
        default="media",
    )
    completada = models.BooleanField(default=False)
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["completada", "fecha_entrega", "titulo"]
        verbose_name = "tarea"
        verbose_name_plural = "tareas"

    def __str__(self):
        return self.titulo