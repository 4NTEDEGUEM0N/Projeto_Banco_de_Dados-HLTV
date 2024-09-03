from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.time_x_partida_schema import TimePartidaCreate, TimePartidaUpdate, TimePartidaResponse
import crud.time_x_partida_crud
from typing import List

router = APIRouter(prefix="/time_x_partida", tags=["Time x Partida"])


@router.post("/", response_model=TimePartidaResponse, status_code=201)
def create_time_partida(time_partida: TimePartidaCreate, db: Session = Depends(get_db)):
    return crud.time_x_partida_crud.create_time_partida(db=db, time_partida=time_partida)


@router.get("/{partida_id}/{time_id}", response_model=TimePartidaResponse, status_code=200)
def get_time_partida(partida_id: int, time_id: int, db: Session = Depends(get_db)):
    db_time_partida = crud.time_x_partida_crud.read_time_partida(db=db, time_id=time_id, partida_id=partida_id)
    print(vars(db_time_partida))
    partidas = TimePartidaResponse.model_validate(db_time_partida)
    for partida in partidas:
        print(partida)
    if db_time_partida is None:
        raise HTTPException(status_code=404, detail="Time Partida not found")
    return db_time_partida


@router.get("/", response_model=List[TimePartidaResponse], status_code=200)
def read_time_partida(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.time_x_partida_crud.read_times_partidas(db, skip=skip, limit=limit)


@router.put("/", response_model=TimePartidaResponse, status_code=200)
def update_time_partida(time_partida: TimePartidaUpdate, db: Session = Depends(get_db)):
    db_time_partida = crud.time_x_partida_crud.read_time_partida(db=db, time_id=time_partida.time_id, partida_id=time_partida.partida_id)
    if db_time_partida is None:
        raise HTTPException(status_code=404, detail="Time Partida not found")
    return crud.time_x_partida_crud.update_time_partida(db, db_time_partida=db_time_partida, time_partida=time_partida)


@router.delete("/{partida_id}/{time_id}", status_code=204)
def delete_time_partida(partida_id: int, time_id: int, db: Session = Depends(get_db)):
    db_time_partida = crud.time_x_partida_crud.read_time_partida(db=db, time_id=time_id, partida_id=partida_id)
    if db_time_partida is None:
        raise HTTPException(status_code=404, detail="Time Partida not found")
    crud.time_x_partida_crud.delete_time_partida(db=db, time_id=time_id, partida_id=partida_id)
