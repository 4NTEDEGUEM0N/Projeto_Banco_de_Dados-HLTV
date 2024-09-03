from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class PartidaSchemaBase(BaseModel):
    data: date
    evento_id: int

class PartidaCreate(PartidaSchemaBase):
    pass

class PartidaUpdate(PartidaSchemaBase):
    pass

class PartidaResponse(PartidaSchemaBase):
    id: int
    evento: Optional["EventoResponseMinimal"]
    time_partida: Optional[List["TimePartidaResponseTimes"]]

    model_config = ConfigDict(from_attributes=True)

class PartidaResponseTimes(BaseModel):
    id: int
    data: date
    time_partida: Optional[List["TimePartidaResponseTimes"]]
    model_config = ConfigDict(from_attributes=True)

class PartidaResponseMinimal(BaseModel):
    id: int
    data: date
    evento: Optional["EventoResponseMinimal"]
    model_config = ConfigDict(from_attributes=True)

from schemas.evento_schema import EventoResponseMinimal
from schemas.time_x_partida_schema import TimePartidaResponseTimes