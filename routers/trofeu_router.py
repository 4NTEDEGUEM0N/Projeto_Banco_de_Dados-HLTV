from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.trofeu_schema import TrofeuResponse, TrofeuCreate, TrofeuUpdate
import crud.trofeu_crud
import crud.evento_crud
from typing import List

router = APIRouter(prefix="/trofeu", tags=["Trofeu"])


@router.post("/", response_model=TrofeuResponse, status_code=201)
def create_trofeu(trofeu: TrofeuCreate, db: Session = Depends(get_db)):
    db_evento = crud.evento_crud.read_evento(db=db, evento_id=trofeu.evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return crud.trofeu_crud.create_trofeu(db=db, trofeu=trofeu)


@router.get("/{evento_id}", response_model=TrofeuResponse, status_code=200)
def get_trofeu(evento_id: int, db: Session = Depends(get_db)):
    db_trofeu = crud.trofeu_crud.read_trofeu(db, evento_id=evento_id)
    if db_trofeu is None:
        raise HTTPException(status_code=404, detail="Trofeu not found")
    return db_trofeu


@router.get("/", response_model=List[TrofeuResponse], status_code=200)
def read_trofeus(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.trofeu_crud.read_trofeus(db, skip=skip, limit=limit)


@router.put("/{evento_id}", response_model=TrofeuResponse, status_code=200)
def update_trofeu(evento_id: int, trofeu_update: TrofeuUpdate, db: Session = Depends(get_db)):
    db_trofeu = crud.trofeu_crud.read_trofeu(db, evento_id=evento_id)
    if db_trofeu is None:
        raise HTTPException(status_code=404, detail="Trofeu not found")
    db_evento = crud.evento_crud.read_evento(db=db, evento_id=trofeu_update.evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return crud.trofeu_crud.update_trofeu(db, db_trofeu=db_trofeu, trofeu=trofeu_update)


@router.delete("/{evento_id}", status_code=204)
def delete_trofeu(evento_id: int, db: Session = Depends(get_db)):
    db_trofeu = crud.trofeu_crud.read_trofeu(db, evento_id=evento_id)
    if db_trofeu is None:
        raise HTTPException(status_code=404, detail="Trofeu not found")
    crud.trofeu_crud.delete_trofeu(db, evento_id=evento_id)
