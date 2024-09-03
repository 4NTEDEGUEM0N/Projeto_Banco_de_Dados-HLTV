from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class TimePartidaSchemaBase(BaseModel):
    partida_id: int
    time_id: int

class TimePartidaCreate(TimePartidaSchemaBase):
    pass

class TimePartidaUpdate(TimePartidaSchemaBase):
    pass

class TimePartidaResponse(TimePartidaSchemaBase):
    partida: Optional["PartidaResponse"]

    model_config = ConfigDict(from_attributes=True)

class TimePartidaResponsePartidas(BaseModel):
    partida: Optional["PartidaResponseMinimal"]
    model_config = ConfigDict(from_attributes=True)

class TimePartidaResponseTimes(BaseModel):
    time: Optional["TimeResponseMinimal"]
    model_config = ConfigDict(from_attributes=True)

from schemas.time_schema import TimeResponseMinimal
from schemas.partida_schema import PartidaResponse
from schemas.partida_schema import PartidaResponseMinimal

