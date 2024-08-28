from sqlalchemy.orm import Session

from models.escalacao_model import EscalacaoModel
from schemas.escalacao_schema import EscalacaoCreate, EscalacaoUpdate


def create_escalacao(db: Session, escalacao: EscalacaoCreate):
    db_escalacao = EscalacaoModel(**escalacao.model_dump())
    db.add(db_escalacao)
    db.commit()
    db.refresh(db_escalacao)
    return db_escalacao


def read_escalacao(db: Session, escalacao_id: int):
    return db.get(EscalacaoModel, escalacao_id)


def read_escalacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(EscalacaoModel).offset(skip).limit(limit).all()


def update_escalacao(db: Session, db_escalacao: EscalacaoModel, escalacao: EscalacaoUpdate):
    for key, value in escalacao.model_dump().items():
        setattr(db_escalacao, key, value)
    db.commit()
    db.refresh(db_escalacao)
    return db_escalacao


def delete_escalacao(db: Session, escalacao_id: int):
    db_escalacao = db.get(EscalacaoModel, escalacao_id)
    db.delete(db_escalacao)
    db.commit()