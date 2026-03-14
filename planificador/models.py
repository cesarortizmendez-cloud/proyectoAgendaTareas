
# Create your models here.
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


class Tarea(models.Model): #modelo para representar las tareas asociadas a una materia
    PRIORIDAD_OPCIONES = [  #definición de las opciones de prioridad para las tareas
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta"),
    ]

    materia = models.ForeignKey( #relación de clave foránea con el modelo
        Materia, 
        on_delete=models.CASCADE, #si se borra una materia, se borran todas sus tareas asociadas
        related_name="tareas"     #permite acceder a las tareas de una materia usando materia.tareas
    )
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    fecha_entrega = models.DateField()
    prioridad = models.CharField(
        max_length=10,
        choices=PRIORIDAD_OPCIONES,
        default="media"
    )
    completada = models.BooleanField(default=False)
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["fecha_entrega", "titulo"]
        verbose_name = "tarea"
        verbose_name_plural = "tareas"

    def __str__(self):
        return self.titulo