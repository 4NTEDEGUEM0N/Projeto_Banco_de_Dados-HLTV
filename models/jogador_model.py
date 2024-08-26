from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class JogadorModel(Base):
    __tablename__ = "jogador"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    nacionalidade = Column(String(255), nullable=False)
    data_nascimento = Column(Date, nullable=False)

    time_id = Column(Integer, ForeignKey("time.id"), nullable=True)
    time = relationship("TimeModel", back_populates="jogadores")