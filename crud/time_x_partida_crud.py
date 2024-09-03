from sqlalchemy.orm import Session

from models.time_x_partida_model import TimePartidaModel
from schemas.time_x_partida_schema import TimePartidaCreate, TimePartidaUpdate


def create_time_partida(db: Session, time_partida: TimePartidaCreate):
    db_time_partida = TimePartidaModel(**time_partida.model_dump())
    db.add(db_time_partida)
    db.commit()
    db.refresh(db_time_partida)
    return db_time_partida


def read_time_partida(db: Session, time_id: int, partida_id: int):
    return db.get(TimePartidaModel, (partida_id, time_id))


def read_times_partidas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TimePartidaModel).offset(skip).limit(limit).all()


def update_time_partida(db: Session, db_time_partida: TimePartidaModel, time_partida: TimePartidaUpdate):
    for key, value in time_partida.model_dump().items():
        setattr(db_time_partida, key, value)
    db.commit()
    db.refresh(db_time_partida)
    return db_time_partida


def delete_time_partida(db: Session, time_id: int, partida_id: int):
    db_time_partida = db.get(TimePartidaModel, (partida_id, time_id))
    db.delete(db_time_partida)
    db.commit()

