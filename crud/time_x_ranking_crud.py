from sqlalchemy.orm import Session

from models.time_x_ranking_model import TimeRankingModel
from schemas.time_x_ranking_schema import TimeRankingCreate, TimeRankingUpdate


def create_time_ranking(db: Session, time_ranking: TimeRankingCreate):
    db_time_ranking = TimeRankingModel(**time_ranking.model_dump())
    db.add(db_time_ranking)
    db.commit()
    db.refresh(db_time_ranking)
    return db_time_ranking


def read_time_ranking(db: Session, time_id: int, ranking_id: int):
    return db.get(TimeRankingModel, (time_id, ranking_id))


def read_times_rankings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TimeRankingModel).offset(skip).limit(limit).all()


def update_time_ranking(db: Session, db_time_ranking: TimeRankingModel, time_ranking: TimeRankingUpdate):
    for key, value in time_ranking.model_dump().items():
        setattr(db_time_ranking, key, value)
    db.commit()
    db.refresh(db_time_ranking)
    return db_time_ranking


def delete_time_ranking(db: Session, time_id: int, ranking_id: int):
    db_time_ranking = db.get(TimeRankingModel, (time_id, ranking_id))
    db.delete(db_time_ranking)
    db.commit()

