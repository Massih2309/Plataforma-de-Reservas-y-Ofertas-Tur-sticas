# 🌴 Plataforma de Reservas y Ofertas Turísticas

Plataforma web para gestionar ofertas turísticas y reservas en República Dominicana.  
Desarrollada con **Reflex (Python)** para el frontend y **FastAPI + MySQL** para el backend.

---

## 📋 Descripción del Proyecto

TurismoRD es una plataforma web que permite a los usuarios:
- Explorar ofertas turísticas en destinos de República Dominicana
- Ver detalles e itinerarios de cada destino
- Realizar reservas de actividades turísticas
- Gestionar reservas a través de una API REST

---

## 🚀 Cómo Instalar y Ejecutar

### Requisitos previos
- Python 3.11+
- MySQL 8+
- Node.js 18+
- Git

### 1. Clonar el repositorio

```bash
git clone https://github.com/Massih2309/Plataforma-de-Reservas-y-Ofertas-Tur-sticas.git
cd Plataforma-de-Reservas-y-Ofertas-Tur-sticas
```

### 2. Backend (FastAPI)

```bash
cd backend/backend

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tu DATABASE_URL

# Iniciar servidor
uvicorn app.main:app --reload --port 8001
```

API disponible en: `http://localhost:8001`  
Documentación: `http://localhost:8001/docs`

### 3. Frontend (Reflex)

```bash
cd frontend/turismo_app

# Instalar dependencias
pip install reflex reflex-base httpx

# Iniciar aplicación
py -m reflex run
```

Frontend disponible en: `http://localhost:3000`

---

## 📁 Estructura de Carpetas

```
Plataforma-de-Reservas-y-Ofertas-Tur-sticas/
│
├── backend/
│   └── backend/
│       ├── app/
│       │   ├── main.py          ← Entrada de la API
│       │   ├── database.py      ← Conexión a MySQL
│       │   ├── models.py        ← Modelos de BD
│       │   ├── schemas.py       ← Validaciones
│       │   └── routers/
│       │       ├── ofertas.py   ← Endpoints de ofertas
│       │       └── reservas.py  ← Endpoints de reservas
│       ├── seed.py              ← Datos de ejemplo
│       ├── requirements.txt
│       └── render.yaml
│
└── frontend/
    └── turismo_app/
        ├── turismo_app/
        │   └── turismo_app.py   ← Página de Inicio
        ├── pages/
        │   ├── descripcion.py   ← Página de Descripción
        │   └── reservas.py      ← Página de Reservas
        └── rxconfig.py
```

---

## 🔌 Endpoints de la API

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/api/ofertas` | Listar todas las ofertas |
| GET | `/api/ofertas?destino=Bavaro` | Filtrar por destino |
| GET | `/api/ofertas/{id}` | Ver oferta por ID |
| POST | `/api/ofertas` | Crear nueva oferta |
| GET | `/api/reservas` | Listar todas las reservas |
| POST | `/api/reservas` | Registrar nueva reserva |
| DELETE | `/api/reservas/{id}` | Cancelar reserva |

---

## 🌿 GitFlow

```
main          ← Producción
develop       ← Integración
feature/backend-api       ← API REST
feature/frontend-reflex   ← Páginas Reflex
```

---

## 🚀 Despliegue

| Servicio | URL |
|---------|-----|
| 🌐 Frontend | https://plataforma-de-reservas-y-ofertas-tur-intl.onrender.com |
| ⚙️ API | https://plataforma-de-reservas-y-ofertas-tur.onrender.com/docs |
| 🗄️ Base de datos | Railway MySQL |

---

## 👥 Créditos

| Rol | Integrante |
|-----|-----------|
| Frontend (Reflex) | Miguel |
| Backend (FastAPI + MySQL) | Massih |

---

## 🔗 Enlaces Útiles

- [Documentación de Reflex](https://reflex.dev/docs/)
- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Render — Despliegue](https://render.com)
- [Railway — Base de datos](https://railway.app)
