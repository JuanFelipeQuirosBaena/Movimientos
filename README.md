# Módulo de Movimientos - Agrosft

## Descripción

El módulo de Movimientos permite registrar las acciones realizadas por los usuarios dentro del sistema. Su objetivo es llevar un control de las operaciones efectuadas para facilitar el seguimiento y la auditoría de las actividades.

---

## Características

- Registro de movimientos.
- Asociación del movimiento con un usuario.
- Clasificación mediante tipos de movimiento.
- Fechas automáticas de creación y actualización.
- Administración desde el panel de Django.

---

## Tecnologías

- Python 3
- Django 4.2
- SQLite3 (desarrollo)
- HTML5
- Bootstrap
- Git

---

## Estructura

```
movimientos/
│
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── urls.py
├── views.py
├── migrations/
└── templates/
```

---

## Modelo de datos

### TipoMovimiento

| Campo | Tipo |
|--------|------|
| nombre | CharField |
| descripcion | TextField |

### Movimiento

| Campo | Tipo |
|--------|------|
| id_movimiento | AutoField |
| tipo_movimiento | ForeignKey |
| usuario | ForeignKey |
| created_at | DateTime |
| updated_at | DateTime |

---

## Flujo del módulo

1. El usuario inicia sesión.
2. Realiza una acción.
3. Se identifica el tipo de movimiento.
4. Se crea el registro.
5. El administrador puede consultar el historial.

---

## Instalación

```bash
git clone <repositorio>

cd dcrm

python -m venv env

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## Autor

Juan Felipe
SENA ADSO

## Arquitectura lógica

                Usuario
                   │
                   ▼
          Interfaz (Templates)
                   │
                   ▼
              Views.py
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
     Movimiento          TipoMovimiento
         │                   │
         └─────────┬─────────┘
                   ▼
             Base de Datos

## Arquitectura por capas

+--------------------------------+
|      Capa de Presentación      |
| Templates (HTML)               |
+--------------------------------+
               │
               ▼
+--------------------------------+
|     Capa de Negocio            |
| Views.py                       |
| Forms.py                       |
+--------------------------------+
               │
               ▼
+--------------------------------+
|      Capa de Datos             |
| Movimiento                     |
| TipoMovimiento                 |
| User (Django)                  |
+--------------------------------+
               │
               ▼
+--------------------------------+
|      Base de Datos SQLite      |
+--------------------------------+

# Modelado UML (Diagrama de clases)

<img width="289" height="283" alt="image" src="https://github.com/user-attachments/assets/48e2041c-5f69-4aa6-989a-ce1917ec1d7a" />
