from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Oferta
from app.schemas import OfertaCreate, OfertaResponse

router = APIRouter()


@router.get("/", response_model=List[OfertaResponse], summary="Listar todas las ofertas")
def listar_ofertas(destino: str = None, db: Session = Depends(get_db)):
    """
    Retorna todas las ofertas turísticas.
    Filtro opcional: ?destino=Bavaro
    """
    query = db.query(Oferta)
    if destino:
        query = query.filter(Oferta.destino.ilike(f"%{destino}%"))
    return query.all()


@router.get("/{oferta_id}", response_model=OfertaResponse, summary="Ver una oferta por ID")
def obtener_oferta(oferta_id: int, db: Session = Depends(get_db)):
    oferta = db.query(Oferta).filter(Oferta.id == oferta_id).first()
    if not oferta:
        raise HTTPException(status_code=404, detail="Oferta no encontrada")
    return oferta


@router.post("/", response_model=OfertaResponse, status_code=201, summary="Crear nueva oferta")
def crear_oferta(oferta: OfertaCreate, db: Session = Depends(get_db)):
    nueva = Oferta(**oferta.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@router.delete("/{oferta_id}", summary="Eliminar una oferta")
def eliminar_oferta(oferta_id: int, db: Session = Depends(get_db)):
    oferta = db.query(Oferta).filter(Oferta.id == oferta_id).first()
    if not oferta:
        raise HTTPException(status_code=404, detail="Oferta no encontrada")
    db.delete(oferta)
    db.commit()
    return {"mensaje": f"Oferta {oferta_id} eliminada correctamente"}
