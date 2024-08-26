from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.jogador_schema import JogadorResponse, JogadorCreate, JogadorUpdate
import crud.jogador_crud as crud
from typing import List

router = APIRouter(prefix="/jogador", tags=["Jogador"])


@router.post("/", response_model=JogadorResponse, status_code=201)
def create_jogador(jogador: JogadorCreate, db: Session = Depends(get_db)):
    return crud.create_jogador(db=db, jogador=jogador)


@router.get("/{jogador_id}", response_model=JogadorResponse, status_code=200)
def get_jogador(jogador_id: int, db: Session = Depends(get_db)):
    db_jogador = crud.read_jogador(db, jogador_id=jogador_id)
    if db_jogador is None:
        raise HTTPException(status_code=404, detail="Jogador not found")
    return db_jogador


@router.get("/", response_model=List[JogadorResponse], status_code=200)
def read_jogadores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_jogadores(db, skip=skip, limit=limit)


@router.put("/{jogador_id}", response_model=JogadorResponse, status_code=200)
def update_jogador(jogador_id: int, jogador_update: JogadorUpdate, db: Session = Depends(get_db)):
    db_jogador = crud.read_jogador(db, jogador_id=jogador_id)
    if db_jogador is None:
        raise HTTPException(status_code=404, detail="Jogador not found")
    return crud.update_jogador(db, db_jogador=db_jogador, jogador=jogador_update)


@router.delete("/{jogador_id}", status_code=204)
def delete_jogador(jogador_id: int, db: Session = Depends(get_db)):
    db_jogador = crud.read_jogador(db, jogador_id=jogador_id)
    if db_jogador is None:
        raise HTTPException(status_code=404, detail="Jogador not found")
    crud.delete_jogador(db, jogador_id=jogador_id)
