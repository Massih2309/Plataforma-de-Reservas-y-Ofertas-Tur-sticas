from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Oferta(Base):
    __tablename__ = "ofertas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=False)
    precio = Column(Float, nullable=False)
    duracion = Column(String(100), nullable=False)   # ej. "3 noches / 4 días"
    destino = Column(String(100), nullable=False)
    imagen_url = Column(String(300), nullable=True)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())


class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    correo = Column(String(150), nullable=False)
    telefono = Column(String(30), nullable=False)
    actividad = Column(String(150), nullable=False)
    fecha = Column(String(20), nullable=False)       # formato YYYY-MM-DD
    metodo_pago = Column(String(50), nullable=False)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())
