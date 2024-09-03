from database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class MapaPartidaModel(Base):
    __tablename__ = 'mapa_partida'
    partida_id = Column(Integer, ForeignKey('partida.id'), primary_key=True)
    mapa_id = Column(Integer, ForeignKey('mapa.id'), primary_key=True)

    partida = relationship("PartidaModel", back_populates="mapa_partida")
    mapa = relationship("MapaModel", back_populates="mapa_partida")