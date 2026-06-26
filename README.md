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

# Modelado UML (Diagrama de clases)

<img width="289" height="283" alt="image" src="https://github.com/user-attachments/assets/48e2041c-5f69-4aa6-989a-ce1917ec1d7a" />

# Modelado UML (Diagrama de componentes)
<img width="251" height="420" alt="image" src="https://github.com/user-attachments/assets/8af83b79-d8ed-4ff6-817b-06ab144940c1" />


# Modelado UML (Diagrama de secuencia)
<img width="458" height="355" alt="image" src="https://github.com/user-attachments/assets/90bdf8f5-cce1-4e40-bca7-dc14c6531f62" />
