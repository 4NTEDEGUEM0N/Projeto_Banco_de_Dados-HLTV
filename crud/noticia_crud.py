from sqlalchemy.orm import Session
from models.noticia_model import NoticiaModel
from schemas.noticia_schema import NoticiaCreate, NoticiaUpdate


def create_noticia(db: Session, noticia: NoticiaCreate):
    db_noticia = NoticiaModel(**noticia.model_dump())
    db.add(db_noticia)
    db.commit()
    db.refresh(db_noticia)
    return db_noticia


def read_noticia(db: Session, noticia_id: int):
    return db.get(NoticiaModel, noticia_id)


def read_noticias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(NoticiaModel).offset(skip).limit(limit).all()


def update_noticia(db: Session, db_noticia: NoticiaModel, noticia: NoticiaUpdate):
    for key, value in noticia.model_dump().items():
        setattr(db_noticia, key, value)
    db.commit()
    db.refresh(db_noticia)
    return db_noticia


def delete_noticia(db: Session, noticia_id: int):
    db_noticia = db.get(NoticiaModel, noticia_id)
    db.delete(db_noticia)
    db.commit()