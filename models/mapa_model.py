from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class MapaModel(Base):
    __tablename__ = "mapa"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    mapa_partida = relationship("MapaPartidaModel", back_populates="mapa")