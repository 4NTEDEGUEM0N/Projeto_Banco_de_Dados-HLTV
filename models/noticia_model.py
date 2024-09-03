from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text



class NoticiaModel(Base):
    __tablename__ = "noticia"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cabecalho = Column(String(100), nullable=False)
    corpo = Column(Text, nullable=False)
    autor = Column(String(100), nullable=False)
    regiao = Column(String(100), nullable=False)
