from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Numeric
from sqlalchemy.orm import relationship


class TrofeuModel(Base):
    __tablename__ = "trofeu"
    evento_id = Column(Integer, ForeignKey('evento.id'), primary_key=True)
    evento = relationship("EventoModel", back_populates="trofeu")

    foto_id = Column(Integer, ForeignKey("foto.id"), nullable=True)
    foto = relationship("FotoModel", back_populates="trofeu")

    jogador_trofeu = relationship('JogadorTrofeuModel', back_populates='trofeu')
    jogador = relationship('JogadorModel', secondary='jogador_trofeu', viewonly=True)