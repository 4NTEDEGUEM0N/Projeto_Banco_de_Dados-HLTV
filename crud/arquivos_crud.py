from sqlalchemy.orm import Session

from models.arquivos_model import FotoModel


def create_arquivo(db: Session, nome_foto: str, dados: bytes, nome: str):
    db_foto = FotoModel(nome_foto=nome_foto, dados=dados, nome=nome)
    db.add(db_foto)
    db.commit()
    db.refresh(db_foto)
    return db_foto


def read_arquivo(db: Session, id_foto: int):
    return db.get(FotoModel, id_foto)


def read_arquivos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(FotoModel).offset(skip).limit(limit).all()


def delete_arquivo(db: Session, id_foto: int):
    db_foto = db.get(FotoModel, id_foto)
    db.delete(db_foto)
    db.commit()