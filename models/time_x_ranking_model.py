from database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship

class TimeRankingModel(Base):
    __tablename__ = 'time_ranking'
    time_id = Column(Integer, ForeignKey('time.id'), primary_key=True)
    ranking_id = Column(Integer, ForeignKey('ranking.id'), primary_key=True)
    posicao = Column(Integer, nullable=False)

    time = relationship("TimeModel", back_populates="time_ranking")
    ranking = relationship("RankingModel", back_populates="time_ranking")

    __table_args__ = (
        UniqueConstraint('time_id', 'ranking_id', 'posicao', name='time_posicao_ranking'),
    )