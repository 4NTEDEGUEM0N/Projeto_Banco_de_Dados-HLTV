from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy import text


def exec_jogador_performance(data_inicio: date, data_final: date, db: Session):
    sql_query = text("SELECT * FROM generate_player_performance_report(:start_date, :end_date)")
    return db.execute(sql_query, {"start_date": data_inicio, "end_date": data_final})


