from database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class JogadorEscalacaoModel(Base):
    __tablename__ = 'escalacao_jogador'
    escalacao_id = Column(Integer, ForeignKey('escalacao.id'), primary_key=True)
    jogador_id = Column(Integer, ForeignKey('jogador.id'), primary_key=True)
    treinador = Column(Boolean, default=False)

    escalacao = relationship("EscalacaoModel", back_populates="escalacao_jogador")
    jogador = relationship("JogadorModel", back_populates="escalacao_jogador")