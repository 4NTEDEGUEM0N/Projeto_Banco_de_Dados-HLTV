from sqlalchemy.orm import Session

from models.mapa_x_partida_model import MapaPartidaModel
from schemas.mapa_x_partida_schema import MapaPartidaCreate, MapaPartidaUpdate


def create_mapa_partida(db: Session, mapa_partida: MapaPartidaCreate):
    db_mapa_partida = MapaPartidaModel(**mapa_partida.model_dump())
    db.add(db_mapa_partida)
    db.commit()
    db.refresh(db_mapa_partida)
    return db_mapa_partida


def read_mapa_partida(db: Session, mapa_id: int, partida_id: int):
    return db.get(MapaPartidaModel, (mapa_id, partida_id))


def read_mapas_partidas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MapaPartidaModel).offset(skip).limit(limit).all()


def update_mapa_partida(db: Session, db_mapa_partida: MapaPartidaModel, mapa_partida: MapaPartidaUpdate):
    for key, value in mapa_partida.model_dump().items():
        setattr(db_mapa_partida, key, value)
    db.commit()
    db.refresh(db_mapa_partida)
    return db_mapa_partida


def delete_mapa_partida(db: Session, mapa_id: int, partida_id: int):
    db_mapa_partida = db.get(MapaPartidaModel, (mapa_id, partida_id))
    db.delete(db_mapa_partida)
    db.commit()

