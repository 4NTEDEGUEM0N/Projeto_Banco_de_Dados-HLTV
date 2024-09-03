from database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class TimePartidaModel(Base):
    __tablename__ = 'time_partida'
    partida_id = Column(Integer, ForeignKey('partida.id'), primary_key=True)
    time_id = Column(Integer, ForeignKey('time.id'), primary_key=True)

    partida = relationship("PartidaModel", back_populates="time_partida")
    time = relationship("TimeModel", back_populates="time_partida")