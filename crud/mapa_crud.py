from sqlalchemy.orm import Session
from models.mapa_model import MapaModel
from schemas.mapa_schema import MapaCreate, MapaUpdate


def create_mapa(db: Session, mapa: MapaCreate):
    db_mapa = MapaModel(**mapa.model_dump())
    db.add(db_mapa)
    db.commit()
    db.refresh(db_mapa)
    return db_mapa


def read_mapa(db: Session, mapa_id: int):
    return db.get(MapaModel, mapa_id)


def read_mapas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MapaModel).offset(skip).limit(limit).all()


def update_mapa(db: Session, db_mapa: MapaModel, mapa: MapaUpdate):
    for key, value in mapa.model_dump().items():
        setattr(db_mapa, key, value)
    db.commit()
    db.refresh(db_mapa)
    return db_mapa


def delete_mapa(db: Session, mapa_id: int):
    db_mapa = db.get(MapaModel, mapa_id)
    db.delete(db_mapa)
    db.commit()