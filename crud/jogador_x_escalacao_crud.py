from sqlalchemy.orm import Session

from models.jogador_x_escalacao_model import JogadorEscalacaoModel
from schemas.jogador_x_escalacao_schema import JogadorEscalacaoCreate, JogadorEscalacaoUpdate


def create_jogador_escalacao(db: Session, jogador_escalacao: JogadorEscalacaoCreate):
    db_jogador_escalacao = JogadorEscalacaoModel(**jogador_escalacao.model_dump())
    db.add(db_jogador_escalacao)
    db.commit()
    db.refresh(db_jogador_escalacao)
    return db_jogador_escalacao


def read_jogador_escalacao(db: Session, jogador_id: int, escalacao_id: int):
    return db.get(JogadorEscalacaoModel, (escalacao_id, jogador_id))


def read_jogadores_escalacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(JogadorEscalacaoModel).offset(skip).limit(limit).all()


def update_jogador_escalacao(db: Session, db_jogador_escalacao: JogadorEscalacaoModel, jogador_escalacao: JogadorEscalacaoUpdate):
    for key, value in jogador_escalacao.model_dump().items():
        setattr(db_jogador_escalacao, key, value)
    db.commit()
    db.refresh(db_jogador_escalacao)
    return db_jogador_escalacao


def delete_jogador_escalacao(db: Session, jogador_id: int, escalacao_id: int):
    db_jogador_escalacao = db.get(JogadorEscalacaoModel, (escalacao_id, jogador_id))
    db.delete(db_jogador_escalacao)
    db.commit()

