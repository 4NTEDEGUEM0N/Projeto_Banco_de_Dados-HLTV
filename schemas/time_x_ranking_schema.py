from typing import Optional, List

from pydantic import BaseModel, ConfigDict



class TimeRankingSchemaBase(BaseModel):
    ranking_id: int
    time_id: int
    posicao: int

class TimeRankingCreate(TimeRankingSchemaBase):
    pass

class TimeRankingUpdate(TimeRankingSchemaBase):
    pass

class TimeRankingResponse(TimeRankingSchemaBase):
    time: Optional["TimeResponseMinimal"]
    ranking: Optional["RankingResponseMinimal"]

    model_config = ConfigDict(from_attributes=True)

class TimeRankingResponseTime(BaseModel):
    time: Optional["TimeResponseMinimal"]
    posicao: int
    model_config = ConfigDict(from_attributes=True)


from schemas.time_schema import TimeResponseMinimal
from schemas.ranking_schema import RankingResponseMinimal