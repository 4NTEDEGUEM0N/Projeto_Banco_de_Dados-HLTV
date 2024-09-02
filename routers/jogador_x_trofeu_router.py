from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.jogador_x_trofeu_schema import JogadorTrofeuCreate, JogadorTrofeuUpdate, JogadorTrofeuResponse
import crud.jogador_x_trofeu_crud
from typing import List

router = APIRouter(prefix="/jogador_x_trofeu", tags=["Jogador x Troféu"])


@router.post("/", response_model=JogadorTrofeuResponse, status_code=201)
def create_jogador_trofeu(jogador_trofeu: JogadorTrofeuCreate, db: Session = Depends(get_db)):
    return crud.jogador_x_trofeu_crud.create_jogador_trofeu(db=db, jogador_trofeu=jogador_trofeu)


@router.get("/{evento_id}/{jogador_id}", response_model=JogadorTrofeuResponse, status_code=200)
def get_jogador_trofeu(evento_id: int, jogador_id: int, db: Session = Depends(get_db)):
    db_jogador_trofeu = crud.jogador_x_trofeu_crud.read_jogador_trofeu(db=db, jogador_id=jogador_id, evento_id=evento_id)
    if db_jogador_trofeu is None:
        raise HTTPException(status_code=404, detail="Jogador Troféu not found")
    return db_jogador_trofeu


@router.get("/", response_model=List[JogadorTrofeuResponse], status_code=200)
def read_jogador_trofeu(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.jogador_x_trofeu_crud.read_jogadores_trofeus(db, skip=skip, limit=limit)


@router.put("/", response_model=JogadorTrofeuResponse, status_code=200)
def update_jogador_trofeu(jogador_trofeu: JogadorTrofeuUpdate, db: Session = Depends(get_db)):
    db_jogador_trofeu = crud.jogador_x_trofeu_crud.read_jogador_trofeu(db=db, jogador_id=jogador_trofeu.jogador_id, evento_id=jogador_trofeu.evento_id)
    if db_jogador_trofeu is None:
        raise HTTPException(status_code=404, detail="Jogador Troféu not found")
    return crud.jogador_x_trofeu_crud.update_jogador_trofeu(db, db_jogador_trofeu=db_jogador_trofeu, jogador_trofeu=jogador_trofeu)


@router.delete("/{evento_id}/{jogador_id}", status_code=204)
def delete_jogador_trofeu(evento_id: int, jogador_id: int, db: Session = Depends(get_db)):
    db_jogador_trofeu = crud.jogador_x_trofeu_crud.read_jogador_trofeu(db=db, jogador_id=jogador_id, evento_id=evento_id)
    if db_jogador_trofeu is None:
        raise HTTPException(status_code=404, detail="Jogador Troféu not found")
    crud.jogador_x_trofeu_crud.delete_jogador_trofeu(db=db, jogador_id=jogador_id, evento_id=evento_id)
