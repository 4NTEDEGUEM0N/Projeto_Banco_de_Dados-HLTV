from sqlalchemy.orm import Session

from models.jogador_x_trofeu_model import JogadorTrofeuModel
from schemas.jogador_x_trofeu_schema import JogadorTrofeuCreate, JogadorTrofeuUpdate


def create_jogador_trofeu(db: Session, jogador_trofeu: JogadorTrofeuCreate):
    db_jogador_trofeu = JogadorTrofeuModel(**jogador_trofeu.model_dump())
    db.add(db_jogador_trofeu)
    db.commit()
    db.refresh(db_jogador_trofeu)
    return db_jogador_trofeu


def read_jogador_trofeu(db: Session, jogador_id: int, evento_id: int):
    return db.get(JogadorTrofeuModel, (jogador_id, evento_id))


def read_jogadores_trofeus(db: Session, skip: int = 0, limit: int = 10):
    return db.query(JogadorTrofeuModel).offset(skip).limit(limit).all()


def update_jogador_trofeu(db: Session, db_jogador_trofeu: JogadorTrofeuModel, jogador_trofeu: JogadorTrofeuUpdate):
    for key, value in jogador_trofeu.model_dump().items():
        setattr(db_jogador_trofeu, key, value)
    db.commit()
    db.refresh(db_jogador_trofeu)
    return db_jogador_trofeu


def delete_jogador_trofeu(db: Session, jogador_id: int, evento_id: int):
    db_jogador_trofeu = db.get(JogadorTrofeuModel, (jogador_id, evento_id))
    db.delete(db_jogador_trofeu)
    db.commit()

