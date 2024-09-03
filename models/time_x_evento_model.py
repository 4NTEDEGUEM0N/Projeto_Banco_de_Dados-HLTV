from database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class TimeEventoModel(Base):
    __tablename__ = 'time_evento'
    evento_id = Column(Integer, ForeignKey('evento.id'), primary_key=True)
    time_id = Column(Integer, ForeignKey('time.id'), primary_key=True)

    evento = relationship("EventoModel", back_populates="time_evento")
    time = relationship("TimeModel", back_populates="time_evento")