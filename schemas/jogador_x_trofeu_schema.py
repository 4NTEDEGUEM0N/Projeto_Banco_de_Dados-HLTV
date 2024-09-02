from typing import Optional

from pydantic import BaseModel, ConfigDict

from schemas.trofeu_schema import TrofeuResponseEvento


class JogadorTrofeuSchemaBase(BaseModel):
    evento_id: int
    jogador_id: int

class JogadorTrofeuCreate(JogadorTrofeuSchemaBase):
    pass

class JogadorTrofeuUpdate(JogadorTrofeuSchemaBase):
    pass

class JogadorTrofeuResponse(JogadorTrofeuSchemaBase):
    jogador: Optional["JogadorResponseMinimal"]
    trofeu: Optional["TrofeuResponseEvento"]

    model_config = ConfigDict(from_attributes=True)

class JogadorTrofeuResponseMinimal(BaseModel):
    trofeu: Optional["TrofeuResponseEvento"]

from schemas.trofeu_schema import TrofeuResponseEvento
from schemas.jogador_schema import JogadorResponseMinimal

