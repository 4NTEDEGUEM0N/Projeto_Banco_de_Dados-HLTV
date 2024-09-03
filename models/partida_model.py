from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class PartidaModel(Base):
    __tablename__ = "partida"
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    evento_id = Column(Integer, ForeignKey("evento.id"), nullable=False)

    evento = relationship("EventoModel", back_populates="partida")
    time_partida = relationship("TimePartidaModel", back_populates="partida")
    mapa_partida = relationship("MapaPartidaModel", back_populates="partida")