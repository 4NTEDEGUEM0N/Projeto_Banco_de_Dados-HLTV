from pydantic import BaseModel, ConfigDict
from typing import List, Optional



class RankingSchemaBase(BaseModel):
    regiao: str

class RankingCreate(RankingSchemaBase):
    pass

class RankingUpdate(RankingSchemaBase):
    pass

class RankingResponse(RankingSchemaBase):
    id: int
    time_ranking: Optional[List["TimeRankingResponseTime"]]

    model_config = ConfigDict(from_attributes=True)

class RankingResponseMinimal(BaseModel):
    id: int
    regiao: str

    model_config = ConfigDict(from_attributes=True)

from schemas.time_x_ranking_schema import TimeRankingResponseTime