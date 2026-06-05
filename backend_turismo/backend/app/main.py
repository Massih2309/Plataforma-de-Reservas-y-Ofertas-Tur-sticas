from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import ofertas, reservas

# Crear tablas al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Turismo App API",
    description="API REST para la Plataforma de Reservas y Ofertas Turísticas",
    version="1.0.0"
)

# CORS — permite que el frontend Reflex se conecte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, cambia esto al dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ofertas.router, prefix="/api/ofertas", tags=["Ofertas"])
app.include_router(reservas.router, prefix="/api/reservas", tags=["Reservas"])

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Turismo App 🌴"}
