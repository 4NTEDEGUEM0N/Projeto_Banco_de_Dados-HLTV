from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class EventoSchemaBase(BaseModel):
    nome: str
    data_inicio: date
    data_fim: date
    pais: str
    presencial: bool
    premiacao: Decimal

class EventoCreate(EventoSchemaBase):
    pass

class EventoUpdate(EventoSchemaBase):
    pass

class EventoResponse(EventoSchemaBase):
    id: int
    trofeu: Optional[List["TrofeuResponseJogador"]] = None

    model_config = ConfigDict(from_attributes=True)

class EventoResponseMinimal(BaseModel):
    id: int
    nome: str

    model_config = ConfigDict(from_attributes=True)


from schemas.trofeu_schema import TrofeuResponseJogador