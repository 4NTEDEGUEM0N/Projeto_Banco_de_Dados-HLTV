from sqlalchemy.orm import Session
from models.time_model import TimeModel
from schemas.time_schema import TimeCreate, TimeUpdate


def create_time(db: Session, time: TimeCreate):
    db_time = TimeModel(**time.model_dump())
    db.add(db_time)
    db.commit()
    db.refresh(db_time)
    return db_time


def read_time(db: Session, time_id: int):
    return db.get(TimeModel, time_id)


def read_times(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TimeModel).offset(skip).limit(limit).all()


def update_time(db: Session, db_time: TimeModel, time: TimeUpdate):
    for key, value in time.model_dump().items():
        setattr(db_time, key, value)
    db.commit()
    db.refresh(db_time)
    return db_time


def delete_time(db: Session, time_id: int):
    db_time = db.get(TimeModel, time_id)
    db.delete(db_time)
    db.commit()