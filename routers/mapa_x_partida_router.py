from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.mapa_x_partida_schema import MapaPartidaCreate, MapaPartidaUpdate, MapaPartidaResponse
import crud.mapa_x_partida_crud
from typing import List

router = APIRouter(prefix="/mapa_x_partida", tags=["Mapa x Partida"])


@router.post("/", response_model=MapaPartidaResponse, status_code=201)
def create_mapa_partida(mapa_partida: MapaPartidaCreate, db: Session = Depends(get_db)):
    return crud.mapa_x_partida_crud.create_mapa_partida(db=db, mapa_partida=mapa_partida)


@router.get("/{partida_id}/{mapa_id}", response_model=MapaPartidaResponse, status_code=200)
def get_mapa_partida(partida_id: int, mapa_id: int, db: Session = Depends(get_db)):
    db_mapa_partida = crud.mapa_x_partida_crud.read_mapa_partida(db=db, mapa_id=mapa_id, partida_id=partida_id)
    if db_mapa_partida is None:
        raise HTTPException(status_code=404, detail="Mapa Partida not found")
    return db_mapa_partida


@router.get("/", response_model=List[MapaPartidaResponse], status_code=200)
def read_mapa_partida(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.mapa_x_partida_crud.read_mapas_partidas(db, skip=skip, limit=limit)


@router.put("/", response_model=MapaPartidaResponse, status_code=200)
def update_mapa_partida(mapa_partida: MapaPartidaUpdate, db: Session = Depends(get_db)):
    db_mapa_partida = crud.mapa_x_partida_crud.read_mapa_partida(db=db, mapa_id=mapa_partida.mapa_id, partida_id=mapa_partida.partida_id)
    if db_mapa_partida is None:
        raise HTTPException(status_code=404, detail="Mapa Partida not found")
    return crud.mapa_x_partida_crud.update_mapa_partida(db, db_mapa_partida=db_mapa_partida, mapa_partida=mapa_partida)


@router.delete("/{partida_id}/{mapa_id}", status_code=204)
def delete_mapa_partida(partida_id: int, mapa_id: int, db: Session = Depends(get_db)):
    db_mapa_partida = crud.mapa_x_partida_crud.read_mapa_partida(db=db, mapa_id=mapa_id, partida_id=partida_id)
    if db_mapa_partida is None:
        raise HTTPException(status_code=404, detail="Mapa Partida not found")
    crud.mapa_x_partida_crud.delete_mapa_partida(db=db, mapa_id=mapa_id, partida_id=partida_id)
