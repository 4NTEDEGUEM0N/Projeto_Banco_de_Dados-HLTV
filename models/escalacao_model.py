from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship


class EscalacaoModel(Base):
    __tablename__ = "escalacao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ativo = Column(Boolean, default=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)

    time_id = Column(Integer, ForeignKey("time.id"), nullable=False)
    time = relationship("TimeModel", back_populates="escalacao")

    escalacao_jogador = relationship('JogadorEscalacaoModel', back_populates='escalacao')
    jogador = relationship('JogadorModel', secondary='escalacao_jogador', viewonly=True)