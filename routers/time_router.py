from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from schemas.time_schema import TimeResponse, TimeCreate, TimeUpdate
import crud.time_crud as crud
from typing import List

router = APIRouter(prefix="/time", tags=["Time"])


@router.post("/", response_model=TimeResponse, status_code=201)
def create_time(time: TimeCreate, db: Session = Depends(get_db)):
    return crud.create_time(db=db, time=time)


@router.get("/{time_id}", response_model=TimeResponse, status_code=200)
def get_time(time_id: int, db: Session = Depends(get_db)):
    db_time = crud.read_time(db, time_id=time_id)
    if db_time is None:
        raise HTTPException(status_code=404, detail="Time not found")
    return db_time


@router.get("/", response_model=List[TimeResponse], status_code=200)
def read_times(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_times(db, skip=skip, limit=limit)


@router.put("/{time_id}", response_model=TimeResponse, status_code=200)
def update_time(time_id: int, time_update: TimeUpdate, db: Session = Depends(get_db)):
    db_time = crud.read_time(db, time_id=time_id)
    if db_time is None:
        raise HTTPException(status_code=404, detail="Time not found")
    return crud.update_time(db, db_time=db_time, time=time_update)


@router.delete("/{time_id}", status_code=204)
def delete_time(time_id: int, db: Session = Depends(get_db)):
    db_time = crud.read_time(db, time_id=time_id)
    if db_time is None:
        raise HTTPException(status_code=404, detail="Time not found")
    crud.delete_time(db, time_id=time_id)
