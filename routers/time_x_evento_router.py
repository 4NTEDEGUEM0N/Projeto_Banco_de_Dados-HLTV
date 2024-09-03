from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.time_x_evento_schema import TimeEventoCreate, TimeEventoUpdate, TimeEventoResponse
import crud.time_x_evento_crud
from typing import List

router = APIRouter(prefix="/time_x_evento", tags=["Time x Evento"])


@router.post("/", response_model=TimeEventoResponse, status_code=201)
def create_time_evento(time_evento: TimeEventoCreate, db: Session = Depends(get_db)):
    return crud.time_x_evento_crud.create_time_evento(db=db, time_evento=time_evento)


@router.get("/{evento_id}/{time_id}", response_model=TimeEventoResponse, status_code=200)
def get_time_evento(evento_id: int, time_id: int, db: Session = Depends(get_db)):
    db_time_evento = crud.time_x_evento_crud.read_time_evento(db=db, time_id=time_id, evento_id=evento_id)
    if db_time_evento is None:
        raise HTTPException(status_code=404, detail="Time Evento not found")
    return db_time_evento


@router.get("/", response_model=List[TimeEventoResponse], status_code=200)
def read_time_evento(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.time_x_evento_crud.read_times_eventos(db, skip=skip, limit=limit)


@router.put("/", response_model=TimeEventoResponse, status_code=200)
def update_time_evento(time_evento: TimeEventoUpdate, db: Session = Depends(get_db)):
    db_time_evento = crud.time_x_evento_crud.read_time_evento(db=db, time_id=time_evento.time_id, evento_id=time_evento.evento_id)
    if db_time_evento is None:
        raise HTTPException(status_code=404, detail="Time Evento not found")
    return crud.time_x_evento_crud.update_time_evento(db, db_time_evento=db_time_evento, time_evento=time_evento)


@router.delete("/{evento_id}/{time_id}", status_code=204)
def delete_time_evento(evento_id: int, time_id: int, db: Session = Depends(get_db)):
    db_time_evento = crud.time_x_evento_crud.read_time_evento(db=db, time_id=time_id, evento_id=evento_id)
    if db_time_evento is None:
        raise HTTPException(status_code=404, detail="Time Evento not found")
    crud.time_x_evento_crud.delete_time_evento(db=db, time_id=time_id, evento_id=evento_id)
