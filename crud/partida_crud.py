from sqlalchemy.orm import Session
from models.partida_model import PartidaModel
from schemas.partida_schema import PartidaCreate, PartidaUpdate


def create_partida(db: Session, partida: PartidaCreate):
    db_partida = PartidaModel(**partida.model_dump())
    db.add(db_partida)
    db.commit()
    db.refresh(db_partida)
    return db_partida


def read_partida(db: Session, partida_id: int):
    return db.get(PartidaModel, partida_id)


def read_partidas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PartidaModel).offset(skip).limit(limit).all()


def update_partida(db: Session, db_partida: PartidaModel, partida: PartidaUpdate):
    for key, value in partida.model_dump().items():
        setattr(db_partida, key, value)
    db.commit()
    db.refresh(db_partida)
    return db_partida


def delete_partida(db: Session, partida_id: int):
    db_partida = db.get(PartidaModel, partida_id)
    db.delete(db_partida)
    db.commit()