from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.mapa_schema import MapaResponse, MapaCreate, MapaUpdate
import crud.mapa_crud as crud
from typing import List

router = APIRouter(prefix="/mapa", tags=["Mapa"])


@router.post("/", response_model=MapaResponse, status_code=201)
def create_mapa(mapa: MapaCreate, db: Session = Depends(get_db)):
    return crud.create_mapa(db=db, mapa=mapa)


@router.get("/{mapa_id}", response_model=MapaResponse, status_code=200)
def get_mapa(mapa_id: int, db: Session = Depends(get_db)):
    db_mapa = crud.read_mapa(db, mapa_id=mapa_id)
    if db_mapa is None:
        raise HTTPException(status_code=404, detail="Mapa not found")
    return db_mapa


@router.get("/", response_model=List[MapaResponse], status_code=200)
def read_mapas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_mapas(db, skip=skip, limit=limit)


@router.put("/{mapa_id}", response_model=MapaResponse, status_code=200)
def update_mapa(mapa_id: int, mapa_update: MapaUpdate, db: Session = Depends(get_db)):
    db_mapa = crud.read_mapa(db, mapa_id=mapa_id)
    if db_mapa is None:
        raise HTTPException(status_code=404, detail="Mapa not found")
    return crud.update_mapa(db, db_mapa=db_mapa, mapa=mapa_update)


@router.delete("/{mapa_id}", status_code=204)
def delete_mapa(mapa_id: int, db: Session = Depends(get_db)):
    db_mapa = crud.read_mapa(db, mapa_id=mapa_id)
    if db_mapa is None:
        raise HTTPException(status_code=404, detail="Mapa not found")
    crud.delete_mapa(db, mapa_id=mapa_id)
