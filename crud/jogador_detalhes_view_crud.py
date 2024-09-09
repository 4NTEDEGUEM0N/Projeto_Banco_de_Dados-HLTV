from sqlalchemy.orm import Session
from models.jogador_detalhes_view import JogadorDetalhesView


def read_jogador_detalhes(db: Session):
    return db.query(JogadorDetalhesView).all()


def read_jogadores_detalhes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(JogadorDetalhesView).offset(skip).limit(limit).all()
