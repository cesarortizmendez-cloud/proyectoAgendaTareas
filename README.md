
proyecto creado por césar ortiz méndez 14/03/2026

sólo para hacer mas fácil las pruebas de la aplicación se registra:
super usuario: cesar1234
pasword: 123456789*

## Objetivo del proyecto

La aplicación permite organizar una agenda de estudio con:

- materias
- tareas asociadas a cada materia
- prioridad
- fecha de entrega
- estado de completitud

Además, el proyecto fue preparado como un entorno de trabajo real, incorporando desde el inicio:

- entorno virtual
- `requirements.txt`
- `.gitignore`
- Git y GitHub
- estructura organizada por proyecto y app
- panel de administración de Django
- CRUD web completo de tareas

---

## Estado actual del proyecto

Hasta este punto, el proyecto ya incluye:

- configuración inicial del entorno
- proyecto Django creado
- app `planificador`
- modelo `Materia`
- modelo `Tarea`
- migraciones iniciales
- administración de datos desde `/admin/`
- vista de inicio
- listado de tareas
- detalle de tarea
- creación de tareas desde la web
- edición de tareas desde la web
- eliminación de tareas desde la web

En otras palabras, ya está implementado el **CRUD completo** de tareas:

- **Crear**
- **Leer**
- **Actualizar**
- **Eliminar**

---

## Tecnologías usadas

- Python
- Django
- SQLite
- HTML con sistema de plantillas de Django
- Git
- GitHub

---

## Estructura del proyecto

```text
agenda-estudio/
├─ .venv/
├─ .git/
├─ .gitignore
├─ requirements.txt
├─ db.sqlite3
├─ manage.py
├─ README.md
├─ agenda_estudio/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
└─ planificador/
   ├─ __init__.py
   ├─ admin.py
   ├─ apps.py
   ├─ forms.py
   ├─ models.py
   ├─ tests.py
   ├─ urls.py
   ├─ views.py
   ├─ migrations/
   │  ├─ __init__.py
   │  └─ 0001_initial.py
   └─ templates/
      └─ planificador/
         ├─ base.html
         ├─ inicio.html
         ├─ lista_tareas.html
         ├─ detalle_tarea.html
         ├─ formulario_tarea.html
         └─ confirmar_eliminar_tarea.html