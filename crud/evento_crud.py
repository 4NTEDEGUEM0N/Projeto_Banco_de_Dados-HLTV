from sqlalchemy.orm import Session
from models.evento_model import EventoModel
from schemas.evento_schema import EventoCreate, EventoUpdate


def create_evento(db: Session, evento: EventoCreate):
    db_evento = EventoModel(**evento.model_dump())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento


def read_evento(db: Session, evento_id: int):
    return db.get(EventoModel, evento_id)


def read_eventos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(EventoModel).offset(skip).limit(limit).all()


def update_evento(db: Session, db_evento: EventoModel, evento: EventoUpdate):
    for key, value in evento.model_dump().items():
        setattr(db_evento, key, value)
    db.commit()
    db.refresh(db_evento)
    return db_evento


def delete_evento(db: Session, evento_id: int):
    db_evento = db.get(EventoModel, evento_id)
    db.delete(db_evento)
    db.commit()