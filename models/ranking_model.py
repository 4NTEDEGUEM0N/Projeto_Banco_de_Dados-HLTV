from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class RankingModel(Base):
    __tablename__ = "ranking"
    id = Column(Integer, primary_key=True, autoincrement=True)
    regiao = Column(String(100), unique=True, nullable=False)

    time_ranking = relationship("TimeRankingModel", back_populates="ranking")