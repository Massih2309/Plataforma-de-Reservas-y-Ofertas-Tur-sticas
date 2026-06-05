from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime
import re


# ── Ofertas ──────────────────────────────────────────────────────────────────

class OfertaBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    duracion: str
    destino: str
    imagen_url: Optional[str] = None


class OfertaCreate(OfertaBase):
    pass


class OfertaResponse(OfertaBase):
    id: int
    creado_en: datetime

    class Config:
        from_attributes = True


# ── Reservas ─────────────────────────────────────────────────────────────────

class ReservaBase(BaseModel):
    nombre: str
    correo: EmailStr
    telefono: str
    actividad: str
    fecha: str          # YYYY-MM-DD
    metodo_pago: str

    @field_validator("fecha")
    @classmethod
    def validar_fecha(cls, v: str) -> str:
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", v):
            raise ValueError("La fecha debe tener formato YYYY-MM-DD")
        return v

    @field_validator("telefono")
    @classmethod
    def validar_telefono(cls, v: str) -> str:
        if not re.match(r"^\+?[\d\s\-]{7,20}$", v):
            raise ValueError("Teléfono inválido")
        return v


class ReservaCreate(ReservaBase):
    pass


class ReservaResponse(ReservaBase):
    id: int
    creado_en: datetime

    class Config:
        from_attributes = True
