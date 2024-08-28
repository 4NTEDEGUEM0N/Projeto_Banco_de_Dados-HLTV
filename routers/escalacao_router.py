from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.escalacao_schema import EscalacaoCreate, EscalacaoUpdate, EscalacaoResponse
import crud.escalacao_crud
from typing import List

router = APIRouter(prefix="/escalacao", tags=["Escalacao"])


@router.post("/", response_model=EscalacaoResponse, status_code=201)
def create_escalacao(escalacao: EscalacaoCreate, db: Session = Depends(get_db)):
    return crud.escalacao_crud.create_escalacao(db=db, escalacao=escalacao)


@router.get("/{escalacao_id}", response_model=EscalacaoResponse, status_code=200)
def get_escalacao(escalacao_id: int, db: Session = Depends(get_db)):
    db_escalacao = crud.escalacao_crud.read_escalacao(db, escalacao_id=escalacao_id)
    if db_escalacao is None:
        raise HTTPException(status_code=404, detail="Escalação not found")
    return db_escalacao


@router.get("/", response_model=List[EscalacaoResponse], status_code=200)
def read_escalacoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.escalacao_crud.read_escalacoes(db, skip=skip, limit=limit)


@router.put("/{escalacao_id}", response_model=EscalacaoResponse, status_code=200)
def update_escalacao(escalacao_id: int, escalacao_update: EscalacaoUpdate, db: Session = Depends(get_db)):
    db_escalacao = crud.escalacao_crud.read_escalacao(db, escalacao_id=escalacao_id)
    if db_escalacao is None:
        raise HTTPException(status_code=404, detail="Escalação not found")
    return crud.escalacao_crud.update_escalacao(db, db_escalacao=db_escalacao, escalacao=escalacao_update)


@router.delete("/{escalacao_id}", status_code=204)
def delete_escalacao(escalacao_id: int, db: Session = Depends(get_db)):
    db_escalacao = crud.escalacao_crud.read_escalacao(db, escalacao_id=escalacao_id)
    if db_escalacao is None:
        raise HTTPException(status_code=404, detail="Escalação not found")
    crud.escalacao_crud.delete_escalacao(db, escalacao_id=escalacao_id)
