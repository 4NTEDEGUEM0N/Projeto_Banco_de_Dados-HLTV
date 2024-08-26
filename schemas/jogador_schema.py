from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Optional


class JogadorSchemaBase(BaseModel):
    name: str
    nacionalidade: str
    data_nascimento: date
    time_id: int | None = None

class JogadorCreate(JogadorSchemaBase):
    pass

class JogadorUpdate(JogadorSchemaBase):
    pass

class JogadorResponse(JogadorSchemaBase):
    id: int
    time: Optional["TimeSchemaBase"] = None

    model_config = ConfigDict(from_attributes=True)

from schemas.time_schema import TimeSchemaBase