from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from datetime import date

from schemas.jogador_performance_procedure_schema import JogadorPerformanceResponse
import crud.jogador_performance_procedure_crud as crud
from typing import List

router = APIRouter(prefix="/procedure", tags=["Procedure"])


@router.get("/PlayerPerformance/Postgres", response_model=List[JogadorPerformanceResponse], status_code=200)
def jogador_performance(data_inicio: date, data_final:date, db: Session = Depends(get_db)):
    return crud.exec_jogador_performance(data_inicio=data_inicio, data_final=data_final, db=db)

