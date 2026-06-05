# 🌴 Plataforma de Reservas y Ofertas Turísticas

Plataforma web para gestionar ofertas turísticas y reservas en República Dominicana.  
Frontend desarrollado con **Reflex (Python)** · Backend con **FastAPI + MySQL** · Desplegado en **Render**.

---

## 📁 Estructura de carpetas

```
turismo_app/               ← Frontend (Reflex)
│   turismo_app/
│   ├── turismo_app.py     ← Página de Inicio
│   ├── pages/
│   │   ├── descripcion.py ← Página de Descripción
│   │   └── reservas.py    ← Página de Reservas
│   ├── assets/
│   └── requirements.txt

backend/                   ← Backend (FastAPI)
├── app/
│   ├── main.py            ← Entrada de la API
│   ├── database.py        ← Conexión a MySQL
│   ├── models.py          ← Tablas (SQLAlchemy)
│   ├── schemas.py         ← Validación (Pydantic)
│   └── routers/
│       ├── ofertas.py     ← Endpoints de ofertas
│       └── reservas.py    ← Endpoints de reservas
├── seed.py                ← Datos de ejemplo
├── requirements.txt
├── render.yaml            ← Config de despliegue
└── .env.example           ← Plantilla de variables de entorno
```

---

## ⚙️ Cómo instalar y ejecutar

### Requisitos previos
- Python 3.11+
- MySQL 8+ (local o en la nube)
- Git

---

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/turismo-app.git
cd turismo-app
```

---

### 2. Backend (FastAPI)

```bash
cd backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Edita .env con tu usuario, contraseña y host de MySQL
```

**Crear la base de datos en MySQL:**

```sql
CREATE DATABASE turismo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Iniciar el servidor:**

```bash
uvicorn app.main:app --reload
```

**Insertar datos de ejemplo (opcional):**

```bash
python seed.py
```

La API estará disponible en `http://localhost:8000`  
Documentación interactiva: `http://localhost:8000/docs`

---

### 3. Frontend (Reflex)

```bash
cd turismo_app

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
reflex run
```

El frontend estará disponible en `http://localhost:3000`

---

## 🔌 Endpoints de la API

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/api/ofertas` | Listar todas las ofertas |
| GET | `/api/ofertas?destino=Bavaro` | Filtrar por destino |
| GET | `/api/ofertas/{id}` | Ver oferta por ID |
| POST | `/api/ofertas` | Crear nueva oferta |
| DELETE | `/api/ofertas/{id}` | Eliminar oferta |
| GET | `/api/reservas` | Listar todas las reservas |
| GET | `/api/reservas/{id}` | Ver reserva por ID |
| POST | `/api/reservas` | Registrar nueva reserva |
| DELETE | `/api/reservas/{id}` | Cancelar reserva |

---

## 🚀 Despliegue en Render

### Backend
1. Crear cuenta en [render.com](https://render.com)
2. **New → Web Service** → conectar repositorio GitHub
3. Configurar:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. En **Environment Variables** agregar `DATABASE_URL` con la URL de tu base de datos MySQL (puedes usar [PlanetScale](https://planetscale.com) o [Railway](https://railway.app) para MySQL gratuito)

### Base de datos MySQL gratuita (Railway)
1. Ir a [railway.app](https://railway.app) → New Project → MySQL
2. Copiar la `DATABASE_URL` que Railway genera
3. Pegarla como variable de entorno en Render

---

## 🌿 GitFlow — Ramas del proyecto

```
main          ← Producción (código estable)
develop       ← Integración de features
feature/backend-api      ← API REST
feature/frontend-inicio  ← Página de inicio
feature/frontend-reservas ← Página de reservas
```

**Flujo de trabajo:**
```bash
git checkout develop
git checkout -b feature/mi-nueva-funcionalidad
# ... desarrollar ...
git push origin feature/mi-nueva-funcionalidad
# Crear Pull Request hacia develop
```

---

## 👥 Créditos

| Rol | Integrante |
|-----|-----------|
| Frontend (Reflex) | [Nombre de tu amigo] |
| Backend (FastAPI + MySQL) | [Tu nombre] |

---

## 🔗 Enlaces útiles

- [Documentación de Reflex](https://reflex.dev/docs/)
- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Render — Despliegue gratuito](https://render.com)
- [Railway — MySQL gratuito](https://railway.app)
- [API Docs (producción)](https://turismo-api.onrender.com/docs)
