from sqlalchemy.orm import Session
from models.trofeu_model import TrofeuModel
from schemas.trofeu_schema import TrofeuCreate, TrofeuUpdate


def create_trofeu(db: Session, trofeu: TrofeuCreate):
    db_trofeu = TrofeuModel(**trofeu.model_dump())
    db.add(db_trofeu)
    db.commit()
    db.refresh(db_trofeu)
    return db_trofeu


def read_trofeu(db: Session, evento_id: int):
    return db.get(TrofeuModel, evento_id)


def read_trofeus(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TrofeuModel).offset(skip).limit(limit).all()


def update_trofeu(db: Session, db_trofeu: TrofeuModel, trofeu: TrofeuUpdate):
    for key, value in trofeu.model_dump().items():
        setattr(db_trofeu, key, value)
    db.commit()
    db.refresh(db_trofeu)
    return db_trofeu


def delete_trofeu(db: Session, evento_id: int):
    db_trofeu = db.get(TrofeuModel, evento_id)
    db.delete(db_trofeu)
    db.commit()