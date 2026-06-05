from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Reserva
from app.schemas import ReservaCreate, ReservaResponse

router = APIRouter()


@router.get("/", response_model=List[ReservaResponse], summary="Listar todas las reservas")
def listar_reservas(db: Session = Depends(get_db)):
    """Retorna el listado completo de reservas registradas."""
    return db.query(Reserva).order_by(Reserva.creado_en.desc()).all()


@router.get("/{reserva_id}", response_model=ReservaResponse, summary="Ver reserva por ID")
def obtener_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reserva


@router.post("/", response_model=ReservaResponse, status_code=201, summary="Registrar nueva reserva")
def crear_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    """
    Registra una nueva reserva turística.
    Valida: formato de correo, teléfono y fecha (YYYY-MM-DD).
    """
    nueva = Reserva(**reserva.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@router.delete("/{reserva_id}", summary="Cancelar una reserva")
def eliminar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    db.delete(reserva)
    db.commit()
    return {"mensaje": f"Reserva {reserva_id} cancelada correctamente"}
