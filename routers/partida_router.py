from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.partida_schema import PartidaResponse, PartidaCreate, PartidaUpdate
import crud.partida_crud as crud
from typing import List

router = APIRouter(prefix="/partida", tags=["Partida"])


@router.post("/", response_model=PartidaResponse, status_code=201)
def create_partida(partida: PartidaCreate, db: Session = Depends(get_db)):
    return crud.create_partida(db=db, partida=partida)


@router.get("/{partida_id}", response_model=PartidaResponse, status_code=200)
def get_partida(partida_id: int, db: Session = Depends(get_db)):
    db_partida = crud.read_partida(db, partida_id=partida_id)
    if db_partida is None:
        raise HTTPException(status_code=404, detail="Partida not found")
    return db_partida


@router.get("/", response_model=List[PartidaResponse], status_code=200)
def read_partidas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_partidas(db, skip=skip, limit=limit)


@router.put("/{partida_id}", response_model=PartidaResponse, status_code=200)
def update_partida(partida_id: int, partida_update: PartidaUpdate, db: Session = Depends(get_db)):
    db_partida = crud.read_partida(db, partida_id=partida_id)
    if db_partida is None:
        raise HTTPException(status_code=404, detail="Partida not found")
    return crud.update_partida(db, db_partida=db_partida, partida=partida_update)


@router.delete("/{partida_id}", status_code=204)
def delete_partida(partida_id: int, db: Session = Depends(get_db)):
    db_partida = crud.read_partida(db, partida_id=partida_id)
    if db_partida is None:
        raise HTTPException(status_code=404, detail="Partida not found")
    crud.delete_partida(db, partida_id=partida_id)
