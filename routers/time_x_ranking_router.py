from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.time_x_ranking_schema import TimeRankingCreate, TimeRankingUpdate, TimeRankingResponse
import crud.time_x_ranking_crud
from typing import List

router = APIRouter(prefix="/time_x_ranking", tags=["Time x Ranking"])


@router.post("/", response_model=TimeRankingResponse, status_code=201)
def create_time_ranking(time_ranking: TimeRankingCreate, db: Session = Depends(get_db)):
    return crud.time_x_ranking_crud.create_time_ranking(db=db, time_ranking=time_ranking)


@router.get("/{ranking_id}/{time_id}", response_model=TimeRankingResponse, status_code=200)
def get_time_ranking(ranking_id: int, time_id: int, db: Session = Depends(get_db)):
    db_time_ranking = crud.time_x_ranking_crud.read_time_ranking(db=db, time_id=time_id, ranking_id=ranking_id)
    if db_time_ranking is None:
        raise HTTPException(status_code=404, detail="Time Ranking not found")
    return db_time_ranking


@router.get("/", response_model=List[TimeRankingResponse], status_code=200)
def read_time_ranking(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.time_x_ranking_crud.read_times_rankings(db, skip=skip, limit=limit)


@router.put("/", response_model=TimeRankingResponse, status_code=200)
def update_time_ranking(time_ranking: TimeRankingUpdate, db: Session = Depends(get_db)):
    db_time_ranking = crud.time_x_ranking_crud.read_time_ranking(db=db, time_id=time_ranking.time_id, ranking_id=time_ranking.ranking_id)
    if db_time_ranking is None:
        raise HTTPException(status_code=404, detail="Time Ranking not found")
    return crud.time_x_ranking_crud.update_time_ranking(db, db_time_ranking=db_time_ranking, time_ranking=time_ranking)


@router.delete("/{ranking_id}/{time_id}", status_code=204)
def delete_time_ranking(ranking_id: int, time_id: int, db: Session = Depends(get_db)):
    db_time_ranking = crud.time_x_ranking_crud.read_time_ranking(db=db, time_id=time_id, ranking_id=ranking_id)
    if db_time_ranking is None:
        raise HTTPException(status_code=404, detail="Time Ranking not found")
    crud.time_x_ranking_crud.delete_time_ranking(db=db, time_id=time_id, ranking_id=ranking_id)
