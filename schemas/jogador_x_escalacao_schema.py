from typing import Optional

from pydantic import BaseModel, ConfigDict



class JogadorEscalacaoSchemaBase(BaseModel):
    escalacao_id: int
    jogador_id: int
    treinador: bool

class JogadorEscalacaoCreate(JogadorEscalacaoSchemaBase):
    pass

class JogadorEscalacaoUpdate(JogadorEscalacaoSchemaBase):
    pass

class JogadorEscalacaoResponse(JogadorEscalacaoSchemaBase):
    jogador: Optional["JogadorResponseMinimal"]
    escalacao: Optional["EscalacaoResponseTime"]

    model_config = ConfigDict(from_attributes=True)

from schemas.escalacao_schema import EscalacaoResponseTime
from schemas.jogador_schema import JogadorResponseMinimal

