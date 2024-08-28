from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.jogador_x_escalacao_schema import JogadorEscalacaoCreate, JogadorEscalacaoUpdate, JogadorEscalacaoResponse
import crud.jogador_x_escalacao_crud
from typing import List

router = APIRouter(prefix="/jogador_x_escalacao", tags=["Jogador x Escalação"])


@router.post("/", response_model=JogadorEscalacaoResponse, status_code=201)
def create_jogador_escalacao(jogador_escalacao: JogadorEscalacaoCreate, db: Session = Depends(get_db)):
    return crud.jogador_x_escalacao_crud.create_jogador_escalacao(db=db, jogador_escalacao=jogador_escalacao)


@router.get("/{escalacao_id}/{jogador_id}", response_model=JogadorEscalacaoResponse, status_code=200)
def get_jogador_escalacao(escalacao_id: int, jogador_id: int, db: Session = Depends(get_db)):
    db_jogador_escalacao = crud.jogador_x_escalacao_crud.read_jogador_escalacao(db=db, jogador_id=jogador_id, escalacao_id=escalacao_id)
    if db_jogador_escalacao is None:
        raise HTTPException(status_code=404, detail="Jogador Escalação not found")
    return db_jogador_escalacao


@router.get("/", response_model=List[JogadorEscalacaoResponse], status_code=200)
def read_jogador_escalacao(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.jogador_x_escalacao_crud.read_jogadores_escalacoes(db, skip=skip, limit=limit)


@router.put("/", response_model=JogadorEscalacaoResponse, status_code=200)
def update_jogador_escalacao(jogador_escalacao: JogadorEscalacaoUpdate, db: Session = Depends(get_db)):
    db_jogador_escalacao = crud.jogador_x_escalacao_crud.read_jogador_escalacao(db=db, jogador_id=jogador_escalacao.jogador_id, escalacao_id=jogador_escalacao.escalacao_id)
    if db_jogador_escalacao is None:
        raise HTTPException(status_code=404, detail="Jogador Escalação not found")
    return crud.jogador_x_escalacao_crud.update_jogador_escalacao(db, db_jogador_escalacao=db_jogador_escalacao, jogador_escalacao=jogador_escalacao)


@router.delete("/{escalacao_id}/{jogador_id}", status_code=204)
def delete_jogador_escalacao(escalacao_id: int, jogador_id: int, db: Session = Depends(get_db)):
    db_jogador_escalacao = crud.jogador_x_escalacao_crud.read_jogador_escalacao(db=db, jogador_id=jogador_id, escalacao_id=escalacao_id)
    if db_jogador_escalacao is None:
        raise HTTPException(status_code=404, detail="Jogador Escalação not found")
    crud.jogador_x_escalacao_crud.delete_jogador_escalacao(db=db, jogador_id=jogador_id, escalacao_id=escalacao_id)
