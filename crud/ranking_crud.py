from sqlalchemy.orm import Session
from models.ranking_model import RankingModel
from schemas.ranking_schema import RankingCreate, RankingUpdate


def create_ranking(db: Session, ranking: RankingCreate):
    db_ranking = RankingModel(**ranking.model_dump())
    db.add(db_ranking)
    db.commit()
    db.refresh(db_ranking)
    return db_ranking


def read_ranking(db: Session, ranking_id: int):
    return db.get(RankingModel, ranking_id)


def read_rankings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RankingModel).offset(skip).limit(limit).all()


def update_ranking(db: Session, db_ranking: RankingModel, ranking: RankingUpdate):
    for key, value in ranking.model_dump().items():
        setattr(db_ranking, key, value)
    db.commit()
    db.refresh(db_ranking)
    return db_ranking


def delete_ranking(db: Session, ranking_id: int):
    db_ranking = db.get(RankingModel, ranking_id)
    db.delete(db_ranking)
    db.commit()