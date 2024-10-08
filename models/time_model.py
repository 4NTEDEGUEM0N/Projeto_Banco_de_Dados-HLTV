from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class TimeModel(Base):
    __tablename__ = "time"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

    escalacao = relationship("EscalacaoModel", back_populates="time")
    time_evento = relationship("TimeEventoModel", back_populates="time")
    time_partida = relationship("TimePartidaModel", back_populates="time")
    time_ranking = relationship("TimeRankingModel", back_populates="time")