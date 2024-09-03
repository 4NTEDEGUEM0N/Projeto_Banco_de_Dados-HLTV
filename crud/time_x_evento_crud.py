from sqlalchemy.orm import Session

from models.time_x_evento_model import TimeEventoModel
from schemas.time_x_evento_schema import TimeEventoCreate, TimeEventoUpdate


def create_time_evento(db: Session, time_evento: TimeEventoCreate):
    db_time_evento = TimeEventoModel(**time_evento.model_dump())
    db.add(db_time_evento)
    db.commit()
    db.refresh(db_time_evento)
    return db_time_evento


def read_time_evento(db: Session, time_id: int, evento_id: int):
    return db.get(TimeEventoModel, (evento_id, time_id))


def read_times_eventos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TimeEventoModel).offset(skip).limit(limit).all()


def update_time_evento(db: Session, db_time_evento: TimeEventoModel, time_evento: TimeEventoUpdate):
    for key, value in time_evento.model_dump().items():
        setattr(db_time_evento, key, value)
    db.commit()
    db.refresh(db_time_evento)
    return db_time_evento


def delete_time_evento(db: Session, time_id: int, evento_id: int):
    db_time_evento = db.get(TimeEventoModel, (evento_id, time_id))
    db.delete(db_time_evento)
    db.commit()

