from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class TimeSchemaBase(BaseModel):
    name: str

class TimeCreate(TimeSchemaBase):
    pass

class TimeUpdate(TimeSchemaBase):
    pass

class TimeResponse(TimeSchemaBase):
    id: int
    escalacao: Optional[List["EscalacaoResponse"]] = None
    time_evento: Optional[List["TimeEventoResponseEvento"]]
    time_partida: Optional[List["TimePartidaResponsePartidas"]]
    time_ranking: Optional[List["TimeRankingResponse"]]

    model_config = ConfigDict(from_attributes=True)

class TimeResponseMinimal(TimeSchemaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


from schemas.escalacao_schema import EscalacaoResponse
from schemas.time_x_evento_schema import TimeEventoResponseEvento
from schemas.time_x_partida_schema import TimePartidaResponsePartidas
from schemas.time_x_ranking_schema import TimeRankingResponse