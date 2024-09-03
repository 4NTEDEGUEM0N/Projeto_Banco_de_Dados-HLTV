from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.noticia_schema import NoticiaResponse, NoticiaCreate, NoticiaUpdate
import crud.noticia_crud as crud
from typing import List

router = APIRouter(prefix="/noticia", tags=["Notícia"])


@router.post("/", response_model=NoticiaResponse, status_code=201)
def create_noticia(noticia: NoticiaCreate, db: Session = Depends(get_db)):
    return crud.create_noticia(db=db, noticia=noticia)


@router.get("/{noticia_id}", response_model=NoticiaResponse, status_code=200)
def get_noticia(noticia_id: int, db: Session = Depends(get_db)):
    db_noticia = crud.read_noticia(db, noticia_id=noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Noticia not found")
    return db_noticia


@router.get("/", response_model=List[NoticiaResponse], status_code=200)
def read_noticias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_noticias(db, skip=skip, limit=limit)


@router.put("/{noticia_id}", response_model=NoticiaResponse, status_code=200)
def update_noticia(noticia_id: int, noticia_update: NoticiaUpdate, db: Session = Depends(get_db)):
    db_noticia = crud.read_noticia(db, noticia_id=noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Noticia not found")
    return crud.update_noticia(db, db_noticia=db_noticia, noticia=noticia_update)


@router.delete("/{noticia_id}", status_code=204)
def delete_noticia(noticia_id: int, db: Session = Depends(get_db)):
    db_noticia = crud.read_noticia(db, noticia_id=noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Noticia not found")
    crud.delete_noticia(db, noticia_id=noticia_id)
