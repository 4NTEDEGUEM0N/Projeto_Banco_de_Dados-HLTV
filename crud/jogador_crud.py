from sqlalchemy.orm import Session
from models.jogador_model import JogadorModel
from schemas.jogador_schema import JogadorCreate, JogadorUpdate


def create_jogador(db: Session, jogador: JogadorCreate):
    db_jogador = JogadorModel(**jogador.model_dump())
    db.add(db_jogador)
    db.commit()
    db.refresh(db_jogador)
    return db_jogador


def read_jogador(db: Session, jogador_id: int):
    return db.get(JogadorModel, jogador_id)


def read_jogadores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(JogadorModel).offset(skip).limit(limit).all()


def update_jogador(db: Session, db_jogador: JogadorModel, jogador: JogadorUpdate):
    for key, value in jogador.model_dump().items():
        setattr(db_jogador, key, value)
    db.commit()
    db.refresh(db_jogador)
    return db_jogador


def delete_jogador(db: Session, jogador_id: int):
    db_jogador = db.get(JogadorModel, jogador_id)
    db.delete(db_jogador)
    db.commit()