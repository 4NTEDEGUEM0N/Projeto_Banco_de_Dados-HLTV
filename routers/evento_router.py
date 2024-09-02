from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.evento_schema import EventoResponse, EventoCreate, EventoUpdate
import crud.evento_crud as crud
from typing import List

router = APIRouter(prefix="/evento", tags=["Evento"])


@router.post("/", response_model=EventoResponse, status_code=201)
def create_evento(evento: EventoCreate, db: Session = Depends(get_db)):
    return crud.create_evento(db=db, evento=evento)


@router.get("/{evento_id}", response_model=EventoResponse, status_code=200)
def get_evento(evento_id: int, db: Session = Depends(get_db)):
    db_evento = crud.read_evento(db, evento_id=evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return db_evento


@router.get("/", response_model=List[EventoResponse], status_code=200)
def read_eventos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_eventos(db, skip=skip, limit=limit)


@router.put("/{evento_id}", response_model=EventoResponse, status_code=200)
def update_evento(evento_id: int, evento_update: EventoUpdate, db: Session = Depends(get_db)):
    db_evento = crud.read_evento(db, evento_id=evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return crud.update_evento(db, db_evento=db_evento, evento=evento_update)


@router.delete("/{evento_id}", status_code=204)
def delete_evento(evento_id: int, db: Session = Depends(get_db)):
    db_evento = crud.read_evento(db, evento_id=evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    crud.delete_evento(db, evento_id=evento_id)
