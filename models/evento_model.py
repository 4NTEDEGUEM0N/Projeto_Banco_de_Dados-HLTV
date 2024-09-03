from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Numeric
from sqlalchemy.orm import relationship


class EventoModel(Base):
    __tablename__ = "evento"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    pais = Column(String(100), nullable=False)
    presencial = Column(Boolean, nullable=False)
    premiacao = Column(Numeric(scale=2), nullable=False)

    trofeu = relationship("TrofeuModel", back_populates="evento")
    time_evento = relationship("TimeEventoModel", back_populates="evento")