from sqlalchemy import Column, Integer, String
from database.database import Base

class PlayerPerformanceReportView(Base):
    __tablename__ = 'player_performance_report'
    __table_args__ = {'extend_existing': True}

    jogador_id = Column(Integer, primary_key=True)
    nome = Column(String)
    apelido = Column(String)
    trofeus_ganhos = Column(Integer)
    escalaoes_ativas = Column(Integer)
    time_atual = Column(String)
    times = Column(String)
