from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class JogadorModel(Base):
    __tablename__ = "jogador"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    apelido = Column(String(100), nullable=False)
    nacionalidade = Column(String(255), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    genero = Column(String(50), nullable=False)

    foto_id = Column(Integer, ForeignKey("foto.id"), nullable=True)
    foto = relationship("FotoModel", back_populates="jogador")

    escalacao_jogador = relationship('JogadorEscalacaoModel', back_populates='jogador')
    jogador_trofeu = relationship('JogadorTrofeuModel', back_populates='jogador')