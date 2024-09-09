from sqlalchemy import Column, Integer, String, Date, LargeBinary
from database.database import Base

class JogadorDetalhesView(Base):
    __tablename__ = "jogador_detalhes_view"
    __table_args__ = {'extend_existing': True}

    jogador_id = Column(Integer, primary_key=True)
    nome_jogador = Column(String)
    apelido = Column(String)
    nacionalidade = Column(String)
    data_nascimento = Column(Date)
    genero = Column(String)
    time_atual = Column(String)
    evento_trofeu = Column(String)
    evento_id = Column(Integer)
    trofeu_foto_id = Column(Integer)
    nome_foto = Column(String)
    foto_id = Column(Integer)
