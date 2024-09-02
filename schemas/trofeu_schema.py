from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class TrofeuSchemaBase(BaseModel):
    evento_id: int
    foto_id: Optional[int] = None

class TrofeuCreate(TrofeuSchemaBase):
    pass

class TrofeuUpdate(TrofeuSchemaBase):
    pass

class TrofeuResponse(TrofeuSchemaBase):
    evento: "EventoResponseMinimal"
    jogador: Optional[List["JogadorResponseMinimal"]] = None

    model_config = ConfigDict(from_attributes=True)

class TrofeuResponseEvento(BaseModel):
    evento: "EventoResponseMinimal"
    model_config = ConfigDict(from_attributes=True)

class TrofeuResponseJogador(BaseModel):
    jogador: Optional[List["JogadorResponseMinimal"]] = None

    model_config = ConfigDict(from_attributes=True)


from schemas.evento_schema import EventoResponseMinimal
from schemas.jogador_schema import JogadorResponseMinimal