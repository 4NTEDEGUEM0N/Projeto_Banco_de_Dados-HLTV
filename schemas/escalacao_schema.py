from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date



class EscalacaoSchemaBase(BaseModel):
    ativo: bool
    data_inicio: date
    data_fim: date
    time_id: int

class EscalacaoCreate(EscalacaoSchemaBase):
    pass

class EscalacaoUpdate(EscalacaoSchemaBase):
    pass

class EscalacaoResponse(EscalacaoSchemaBase):
    id: int
    jogador: Optional[List["JogadorResponseMinimal"]] = None

    model_config = ConfigDict(from_attributes=True)

class EscalacaoResponseTime(BaseModel):
    time: Optional["TimeResponseMinimal"]
    model_config = ConfigDict(from_attributes=True)

from schemas.jogador_schema import JogadorResponseMinimal
from schemas.time_schema import TimeResponseMinimal