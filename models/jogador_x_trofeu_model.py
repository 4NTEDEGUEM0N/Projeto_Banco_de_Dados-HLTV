from database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class JogadorTrofeuModel(Base):
    __tablename__ = 'jogador_trofeu'
    evento_id = Column(Integer, ForeignKey('trofeu.evento_id'), primary_key=True)
    jogador_id = Column(Integer, ForeignKey('jogador.id'), primary_key=True)

    trofeu = relationship("TrofeuModel", back_populates="jogador_trofeu")
    jogador = relationship("JogadorModel", back_populates="jogador_trofeu")