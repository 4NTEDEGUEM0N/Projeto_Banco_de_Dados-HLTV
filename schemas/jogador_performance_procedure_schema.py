from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class JogadorPerformanceResponse(BaseModel):
    jogador_id: int
    nome: str
    apelido: str
    trofeus_ganhos: int
    escalaoes_ativas: int
    time_atual: Optional[str]
    times: Optional[str]

    model_config = ConfigDict(from_attributes=True)
