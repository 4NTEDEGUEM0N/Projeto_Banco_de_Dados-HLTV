from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.jogador_detalhes_view_schema import JogadorDetalhesResponse
import crud.jogador_detalhes_view_crud as crud
from typing import List

router = APIRouter(prefix="/view", tags=["View"])


@router.get("/jogador_detalhes/all", response_model=List[JogadorDetalhesResponse], status_code=200)
def get_jogador_detalhes(db: Session = Depends(get_db)):
    db_jogador_detalhes = crud.read_jogador_detalhes(db)
    if db_jogador_detalhes is None:
        raise HTTPException(status_code=404, detail="Jogador not found")
    return db_jogador_detalhes


@router.get("/jogador_detalhes", response_model=List[JogadorDetalhesResponse], status_code=200)
def read_jogadores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_jogadores_detalhes(db, skip=skip, limit=limit)

