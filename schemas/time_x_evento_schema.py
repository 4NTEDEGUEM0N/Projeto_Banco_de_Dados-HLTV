from typing import Optional

from pydantic import BaseModel, ConfigDict



class TimeEventoSchemaBase(BaseModel):
    evento_id: int
    time_id: int

class TimeEventoCreate(TimeEventoSchemaBase):
    pass

class TimeEventoUpdate(TimeEventoSchemaBase):
    pass

class TimeEventoResponse(TimeEventoSchemaBase):
    evento: Optional["EventoResponseMinimal"]
    time: Optional["TimeResponseMinimal"]

    model_config = ConfigDict(from_attributes=True)

class TimeEventoResponseTime(BaseModel):
    time: Optional["TimeResponseMinimal"]
    model_config = ConfigDict(from_attributes=True)

class TimeEventoResponseEvento(BaseModel):
    evento: Optional["EventoResponseMinimal"]
    model_config = ConfigDict(from_attributes=True)

from schemas.time_schema import TimeResponseMinimal
from schemas.evento_schema import EventoResponseMinimal


