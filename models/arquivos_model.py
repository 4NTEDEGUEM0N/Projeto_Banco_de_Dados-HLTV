from sqlalchemy import Column, Integer, String, LargeBinary
from database.database import Base
from sqlalchemy.orm import relationship

class FotoModel(Base):
    __tablename__ = "foto"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    nome_foto = Column(String, nullable=False)
    dados = Column(LargeBinary, nullable=False)

    jogador = relationship("JogadorModel", back_populates="foto")
