from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.ranking_schema import RankingResponse, RankingCreate, RankingUpdate
import crud.ranking_crud as crud
from typing import List

router = APIRouter(prefix="/ranking", tags=["Ranking"])


@router.post("/", response_model=RankingResponse, status_code=201)
def create_ranking(ranking: RankingCreate, db: Session = Depends(get_db)):
    return crud.create_ranking(db=db, ranking=ranking)


@router.get("/{ranking_id}", response_model=RankingResponse, status_code=200)
def get_ranking(ranking_id: int, db: Session = Depends(get_db)):
    db_ranking = crud.read_ranking(db, ranking_id=ranking_id)
    if db_ranking is None:
        raise HTTPException(status_code=404, detail="Ranking not found")
    return db_ranking


@router.get("/", response_model=List[RankingResponse], status_code=200)
def read_rankings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_rankings(db, skip=skip, limit=limit)


@router.put("/{ranking_id}", response_model=RankingResponse, status_code=200)
def update_ranking(ranking_id: int, ranking_update: RankingUpdate, db: Session = Depends(get_db)):
    db_ranking = crud.read_ranking(db, ranking_id=ranking_id)
    if db_ranking is None:
        raise HTTPException(status_code=404, detail="Ranking not found")
    return crud.update_ranking(db, db_ranking=db_ranking, ranking=ranking_update)


@router.delete("/{ranking_id}", status_code=204)
def delete_ranking(ranking_id: int, db: Session = Depends(get_db)):
    db_ranking = crud.read_ranking(db, ranking_id=ranking_id)
    if db_ranking is None:
        raise HTTPException(status_code=404, detail="Ranking not found")
    crud.delete_ranking(db, ranking_id=ranking_id)
