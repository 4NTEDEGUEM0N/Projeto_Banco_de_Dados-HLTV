from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy import text
from models.jogador_performance_view import PlayerPerformanceReportView
from sqlalchemy.future import select


def exec_jogador_performance(db: Session):
    sql_query = text("SELECT * FROM generate_player_performance_report()")
    return db.execute(sql_query)


def read_jogador_performance_report(db: Session):
    return db.query(PlayerPerformanceReportView).all()

