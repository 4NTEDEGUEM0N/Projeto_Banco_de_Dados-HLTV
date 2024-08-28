from sqlalchemy.orm import Session

from models.arquivos_model import ArquivoModel


def create_arquivo(db: Session, nome_arquivo: str, dados: bytes, nome: str):
    db_arquivo = ArquivoModel(nome_arquivo=nome_arquivo, dados=dados, nome=nome)
    db.add(db_arquivo)
    db.commit()
    db.refresh(db_arquivo)
    return db_arquivo


def read_arquivo(db: Session, id_arquivo: int):
    return db.get(ArquivoModel, id_arquivo)

def delete_arquivo(db: Session, id_arquivo: int):
    db_arquivo = db.get(ArquivoModel, id_arquivo)
    db.delete(db_arquivo)
    db.commit()