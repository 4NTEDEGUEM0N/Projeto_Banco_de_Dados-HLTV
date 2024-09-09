from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Optional

class JogadorDetalhesResponse(BaseModel):
    jogador_id: int
    nome_jogador: str
    apelido: str
    nacionalidade: str
    data_nascimento: date
    genero: str
    time_atual: Optional[str]
    evento_trofeu: Optional[str]
    evento_id: Optional[int]
    trofeu_foto_id: Optional[int]
    nome_foto: Optional[str]
    foto_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)
