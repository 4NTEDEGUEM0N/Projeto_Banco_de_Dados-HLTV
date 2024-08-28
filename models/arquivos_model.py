from sqlalchemy import Column, Integer, String, LargeBinary
from database.database import Base

class ArquivoModel(Base):
    __tablename__ = "arquivos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    nome_arquivo = Column(String, nullable=False)
    dados = Column(LargeBinary, nullable=False)
